from django.urls import path

from VideoProcessing.controller.signup_controller import SignUpController

urlpatterns = [
    path('', SignUpController.as_view())
]