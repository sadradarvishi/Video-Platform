from django.urls import path

from VideoProcessing.controller.video_upload_controller import VideoUploadController


urlpatterns = [
    path('', VideoUploadController.as_view())
]