from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response

from VideoProcessing.logic.login_logic import LoginLogic

class LoginController(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.login_logic = LoginLogic()

    def post(self, request):
        try:
            data = request.data
            username = data.get('username')
            password = data.get('password')

            checked_password = self.login_logic.password_checker(username, password)

            if not checked_password:
                return Response({"Message":"Username or Password is incorrect!"})

            tokens = self.login_logic.generate_token(username)

            return Response(tokens, HTTP_200_OK)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)

