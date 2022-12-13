from django.urls import path, include
from rest_framework import routers
from .views import JobApiView

router = routers.DefaultRouter()
router.register(r'jobs', JobApiView, basename="jobs")

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]




