import logging
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    UploadSerializer,
    JobSerializer,
    UpdateJobSerializer
)
from rest_framework.viewsets import ViewSet
from .models import Job
from .task import process_image


class JobApiView(ViewSet):

    serializer_class = UploadSerializer

    def retrieve(self, request, pk=None):
        """
        Check the status of a job
        """
        try:
            queryset = Job.objects.get(id=pk)
            serializer = JobSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            logging.exception('Exception in {}'.format(
                self.__class__.__name__))
            return Response(
                {'message': 'Bad Request'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        """
        Create a new job to procreate an image.
        """
        try:
            file_uploaded = request.FILES.get('file')
            #  Creating a new job to process the image
            new_job = Job.objects.create(image_url=file_uploaded)
            new_job.save()
            # Execute celery task
            process_image.delay(job_id=new_job.id)
            response = {'job_id': new_job.id}
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception:
            logging.exception('Exception in {}'.format(
                self.__class__.__name__))
            return Response(
                {'message': 'Bad Request'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk=None):
        """
        Changes the status of a job to the step the user wants.
        """
        try:
            action = request.data.get('action')
            process_image(job_id=pk, execute_actions=action)
            update_job = Job.objects.get(id=pk)
            serializer = UpdateJobSerializer(update_job)
            return Response(serializer.data)
        except Exception:
            logging.exception('Exception in {}'.format(
                self.__class__.__name__))
            return Response(
                {'message': 'Bad Request'},
                status=status.HTTP_400_BAD_REQUEST
            )
