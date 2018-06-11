from django.urls import path, include
from rest_framework import routers

from .views import PulseUploadView, PulseDownloadView, PulseViewSet


router = routers.SimpleRouter()
router.register('pulse', PulseViewSet)

urlpatterns = [
    path(r'pulse/upload/', PulseUploadView.as_view(), name='pulse_upload'),
    path(r'pulse/download/', PulseDownloadView.as_view(), name='pulse_download'),
    path(r'', include((router.urls, 'pulse'))),

]