from rest_framework import serializers
from api.models import (
    Job,
    Step,
)


class StepSerializer(serializers.ModelSerializer):

    step = serializers.SerializerMethodField()

    def get_step(self, obj):
        return obj.description

    class Meta:
        model = Step
        fields = [
            'step',
            'status',
            'start_date',
            'end_date'
        ]


class JobSerializer(serializers.ModelSerializer):

    steps = serializers.SerializerMethodField()

    job_id = serializers.SerializerMethodField()

    def get_steps(self, obj):
        steps_query = Step.objects.filter(jobs_id=obj.id).all()
        if steps_query:
            return StepSerializer(steps_query, many=True).data
        return None

    def get_job_id(self, obj):
        return obj.id

    class Meta:
        model = Job
        fields = [
            'job_id',
            'steps',
        ]


class UpdateJobSerializer(serializers.ModelSerializer):

    steps = serializers.SerializerMethodField()

    job_id = serializers.SerializerMethodField()

    def get_steps(self, obj):
        steps_query = Step.objects.filter(
            jobs_id=obj.id).order_by('-id').all()[:2]
        if steps_query:
            return StepSerializer(steps_query, many=True).data
        return None

    def get_job_id(self, obj):
        return obj.id

    class Meta:
        model = Job
        fields = [
            'job_id',
            'steps',
        ]


class LogSerializer(serializers.ModelSerializer):
    step = StepSerializer(read_only=True)
    job = JobSerializer(read_only=True)

    class Meta:
        model = Job
        fields = [
            'job',
            'step',
            'error'
        ]


class UploadSerializer(serializers.ModelSerializer):
    file_uploaded = serializers.FileField(
        required=True
    )

    class Meta:
        fields = ['file_uploaded']