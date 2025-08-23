from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from VideoProcessing.dao.user_dao import UserDao

class EditUserLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_dao = UserDao()

    def edit_profile(self, data, user, picture):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        phone_number = data.get('phone_number')
        username = data.get('username')

        return self.user_dao.edit_user(
            user=user,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            username=username,
            picture=picture
        )

