import datetime
import logging
import uuid
from django.db import models

STEPS_CHOICES = {
        'invert_colors': 'Invertir Colores',
        'black_and_white': 'Pasar a Blanco y Negro',
        'rotate_image': 'Rotar la imagen 90 grados',
        'invert_vertical_axis': 'E invertir la sobre el eje vertical.'
}

STATUS_CHOICES = {
    'successful': 'SUCCESSFUL',
    'process': 'PROCESS',
    'fail': 'FAIL'
}


class TimeStampModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def upload_to(instance, filename):
    return '{filename}'.format(filename=filename)


class Job(TimeStampModel):
    job_id = models.UUIDField(
         default=uuid.uuid4,
         editable=False
    )
    image_url = models.ImageField(
        upload_to=upload_to,
        blank=True,
        null=True
    )


class Step(models.Model):
    description = models.CharField(
        max_length=50,
        default=STEPS_CHOICES.get('invert_colors')
    )
    status = models.CharField(
        max_length=50,
        default=STATUS_CHOICES.get('process')
    )
    jobs = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    start_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    end_date = models.DateTimeField(
        blank=True,
        null=True
    )

    @staticmethod
    def create_step(job, step_code, status_code):
        try:
            step = Step(
                description=STEPS_CHOICES.get(step_code),
                status=STATUS_CHOICES.get(status_code),
                jobs=job
            )
            step.save()
            return step
        except Exception:
            logging.exception('Exception in Step Model')
            return None

    @staticmethod
    def update_step(job, fail=False):
        if not fail:
            job.status = 'successful'
        else:
            job.status = 'failed'
        job.end_date = datetime.datetime.today()
        job.save()


class Log(TimeStampModel):
    jobs = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    steps = models.ForeignKey(
        Step,
        on_delete=models.CASCADE
    )
    error = models.CharField(
        max_length=250,
        null=True
    )


