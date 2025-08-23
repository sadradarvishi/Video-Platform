from django.contrib.auth.hashers import  check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from VideoProcessing.dao.user_dao import UserDao

class EditPasswordLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_dao = UserDao()

    def edit_password(self, data, user):
        old_password = data.get("old_password")
        new_password = data.get("new_password")

        check_pass = check_password(old_password, user.password)

        if not check_pass:
            raise ValidationError("Wrong password")

        try:
            validate_password(new_password)
        except Exception as e:
            raise ValidationError(str(e))

        return self.user_dao.edit_password(password=new_password, user=user)


