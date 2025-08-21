from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserEntity(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=225, null=False)
    last_name = models.CharField(max_length=225, null=False)
    phone_number = models.CharField(null=False, unique=True)
    username = models.CharField(max_length=225, null=False, unique=True)
    password = models.CharField(max_length=225, null=False, blank=False)
    picture = models.ImageField(upload_to='user_picture/', null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    is_premium = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'


    def __str__(self):
        return self.username
