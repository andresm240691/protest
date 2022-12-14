import uuid
import logging
from .models import Step
from PIL import Image, ImageChops
from protest.settings import MEDIA_ROOT


def invert_colors(job):
    """
    Step 1: Invert the colors
    :params job {Queryset}
    """
    execute_status = False

    # Create initial step IN PROCESS
    step_query = Step.create_step(
        job=job,
        status_code='process',
        step_code='invert_colors'
    )
    try:
        import pudb;pudb.set_trace()
        img = Image.open(job.image_url.path)
        inv_img = ImageChops.invert(img)
        new_img_name = str(uuid.uuid4()) + '.' + img.format
        new_path = '{media_root}/{filename}'.format(
            media_root=MEDIA_ROOT, filename=new_img_name)
        inv_img.save(new_path)
        job.image_url.detele()
        job.image_url = new_path
        job.save()
        # Update Step
        execute_status = True
        step_query.update_step(job=job, fail=False)
    except Exception:
        step_query.update_step(job=job, fail=True)
        logging.exception('Exception in invert_colors')

    return execute_status


def black_and_white(job):
    response = {'status': False, 'image': None}
    try:
        pass
    except Exception:
        logging.exception('Exception in black_and_white')
    finally:
        return response


def rotate_image(job):
    response = {'status': False, 'image': None}
    try:
        pass
    except Exception:
        logging.exception('Exception in rotate_image')
    finally:
        return response


def invert_vertical_axis(job):
    response = {'status': False, 'image': None}
    try:
        pass
    except Exception:
        logging.exception('Exception in invert_vertical_axis')
    finally:
        return response