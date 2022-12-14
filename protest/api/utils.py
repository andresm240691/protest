import uuid
import logging
from PIL import Image, ImageChops
from protest.settings import MEDIA_ROOT
from .models import Log, STEPS_CHOICES


def transform_image(job, action):
    """
    function to apply the following transformations
    1. Invert the colors
    2. Go to Black and White
    3. Rotate the image 90 degrees
    4. And invert the about the vertical axis.
    :params job {Queryset}
    :params action {String}
    :return response {object}
    """
    response = {'execute_status': 'successful', 'job': job}

    try:
        img = Image.open(job.image_url.path)
        if action == 'invert_colors':
            new_image = ImageChops.invert(img)
        if action == 'black_and_white':
            new_image = img.convert("1")
        if action == 'rotate_image':
            new_image = img.rotate(90)
        if action == 'invert_vertical_axis':
            new_image = img.transpose(Image.TRANSPOSE)

        new_img_name = str(uuid.uuid4()) + '.' + img.format
        new_path = '{media_root}/{filename}'.format(
            media_root=MEDIA_ROOT, filename=new_img_name)
        new_image.save(new_path)

        job.image_url.delete()
        job.image_url = new_path
        job.save()

        # Update Step
        response.update(job=job)

    except Exception as e:
        log_query = Log(
            job_id=job.id,
            error=str(e),
            step_description=STEPS_CHOICES.get(action)
        )
        log_query.save()
        response.update(execute_status='fail', job=job)
        logging.exception('Exception in transform_image')

    return response
