import logging
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadSerializer
from rest_framework.viewsets import ViewSet
from .models import Job


class JobApiView(ViewSet):

    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        try:
            import pudb;pudb.set_trace()
            file_uploaded = request.FILES.get('file')
            new_job = Job.objects.create(image_url=file_uploaded)
            new_job.save()

            content_type = file_uploaded.content_type
            response = "POST API and you have uploaded a {} file".format(
                content_type)
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception:
            logging.exception('Exception in {}'.format(
                self.__class__.__name__))