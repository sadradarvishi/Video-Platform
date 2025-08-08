from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from VideoProcessing.dao.signup_dao import SignUpDao

class SignUpLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signup_dao = SignUpDao()

    def create_user(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        phone_number = data.get('phone_number')
        username = data.get('username')
        password = data.get('password')
        picture = data.get('picture')

        try:
            validate_password(password)
        except Exception as e:
            raise ValidationError(str(e))

        hashed_password = make_password(password)

        return self.signup_dao.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            username=username,
            password=hashed_password,
            picture=picture
        )