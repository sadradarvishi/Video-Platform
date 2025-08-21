from django.urls import path

from VideoProcessing.controller.user_controller import UserController

urlpatterns = [
    path('', UserController.as_view())
]