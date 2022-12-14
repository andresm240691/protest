import logging
from celery import shared_task
from .models import Job, Step, Log
from .utils import transform_image
from django.utils import timezone


@shared_task
def process_image(job_query, execute_actions='all'):
    stop_execute = False
    print("Execute celery")
    list_actions = [execute_actions] if execute_actions != 'all' else [
        'invert_colors', 'black_and_white', 'rotate_image',
        'invert_vertical_axis']

    for action in list_actions:
        try:
            # Register initial state of step
            step_query = Step.create_step(
                job=job_query,
                status_code='process',
                step_code=action
            )

            result = transform_image(job_query, action)
            if result.get('execute_status') == 'successful':
                job_query = result.get('job')
                print("Success Execute JOB ID {} STEP: {}".format(
                    job_query.id, 'invert_colors'))
            else:
                stop_execute = True
                print("Fail Execute JOB ID {} STEP: {}".format(
                    job_query.id, 'invert_colors'))

            # register final statusof step
            step_query = Step.create_step(
                job=result.get('job'),
                status_code=result.get('execute_status'),
                step_code=action,
                end_date=timezone.now()
            )

            if stop_execute:
                break

        except Exception as e:
            logging.exception('Exception in process_image')
            print("Exception in process_image:" + str(e))
