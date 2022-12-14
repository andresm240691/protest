import logging
from celery import shared_task
from .models import Job, Step, Log
from .utils import (
    invert_colors,
    black_and_white,
    rotate_image,
    invert_vertical_axis
)


#@shared_task
def process_image(job_query):
    stop_execute = False
    try:
        if job_query:
            # Step 1: Invert Colors
            if not stop_execute:
                result = invert_colors(job_query)
                if result:
                    print("Success Execute JOB ID {} STEP: {}".format(
                        job_query.id, 'invert_colors'))
                else:
                    stop_execute = False
                    print("Fail Execute JOB ID {} STEP: {}".format(
                        job_query.id, 'invert_colors'))

    except Exception as e:
        logging.exception('Exception in process_image')
        print("Exception in process_image:" + str(e))
