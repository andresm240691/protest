import logging
from celery import shared_task
from .models import Job, Step, Log
from .utils import transform_image
from django.utils import timezone


@shared_task
def process_image(job_id, execute_actions='all'):
    stop_execute = False
    print("############ Execute Celery Task #################")
    list_actions = [execute_actions] if execute_actions != 'all' else [
        'invert_colors', 'black_and_white', 'rotate_image',
        'invert_vertical_axis']

    job_query = Job.objects.get(id=job_id)
    if job_query:
        print("JOB ID: {}".format(job_id))
        for action in list_actions:
            print("applied transform: {}".format(action))
            try:
                # Register initial state of step
                step_query = Step.create_step(
                    job=job_query,
                    status_code='process',
                    step_code=action
                )

                result = transform_image(job_query, action)
                if result.get('execute_status') == 'successful':
                    print("Success Execute")
                else:
                    stop_execute = True
                    print("Fail Execute")

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
