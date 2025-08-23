from django.urls import path

from VideoProcessing.controller.user_controller import UserController
from VideoProcessing.controller.edit_user_controller import EditUserController
from VideoProcessing.controller.edit_password_controller import EditPasswordController

urlpatterns = [
    path('', UserController.as_view()),
    path('edit/', EditUserController.as_view()),
    path('edit/password/', EditPasswordController.as_view()),
]
