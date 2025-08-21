from django.urls import path

from VideoProcessing.controller.video_controller import VideoController

urlpatterns = [
    path('', VideoController.as_view())
]