import uuid
from django.db import models

STEPS_CHOICES = [
        ('invert_colors', 'Invertir Colores'),
        ('black_and_white', 'Pasar a Blanco y Negro'),
        ('rotate_image', 'Rotar la imagen 90 grados'),
        ('invert_vertical_axis', 'E invertir la sobre el eje vertical.')
    ]

STATUS_CHOICES = [
    ('successful', 'SUCCESSFUL'),
    ('in_process', 'IN PROCESS'),
    ('processed', 'Processed'),
    ('failed', 'Failed'),
]


class TimeStampModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Job(TimeStampModel):
    job_id = models.UUIDField(
         default=uuid.uuid4,
         editable=False
    )
    img_src = models.CharField(
        null=True,
        blank=True,
        max_length=250
    )


class Step(models.Model):
    description = models.CharField(
        max_length=50,
        choices=STEPS_CHOICES,
        default='invert_colors'
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='process'
    )
    jobs = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    start_date = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )
    end_date = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )


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


