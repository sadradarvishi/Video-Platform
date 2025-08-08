from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

from VideoProcessing.dao.login_dao import LoginDao

class LoginLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.login_dao = LoginDao()

    def password_checker(self, username, password):
        user = self.login_dao.get_user_by_username(username=username)
        return check_password(password, user.password)

    def generate_token(self, username):
        user = self.login_dao.get_user_by_username(username=username)

        refresh_token = RefreshToken.for_user(user)

        return {
            'access': str(refresh_token.access_token),
            'refresh': str(refresh_token)
        }
