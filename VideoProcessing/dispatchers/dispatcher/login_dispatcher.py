from django.urls import path

from VideoProcessing.controller.login_controller import LoginController

urlpatterns = [
    path('', LoginController.as_view())
]