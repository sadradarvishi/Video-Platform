from VideoProcessing.entity.user_entity import UserEntity

from typing import Optional
from django.core.files.uploadedfile import UploadedFile

class SignUpDao:

    def create_user(
            self,
            first_name,
            last_name,
            phone_number,
            username,
            password,
            picture: Optional[UploadedFile]
    ):
        return UserEntity.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            username=username,
            password=password,
            picture=picture
        )
