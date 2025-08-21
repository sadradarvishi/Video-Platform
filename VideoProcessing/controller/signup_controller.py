from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from VideoProcessing.logic.signup_logic import SignUpLogic

class SignUpController(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signup_logic = SignUpLogic()

    def post(self, request):
        try:
            data = request.data
            self.signup_logic.create_user(data)

            return Response(None, HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)

