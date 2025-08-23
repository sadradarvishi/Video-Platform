from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from VideoProcessing.logic.edit_password_logic import EditPasswordLogic

class EditPasswordController(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.edit_password_logic = EditPasswordLogic()

    def patch(self,request):
        try:
            data = request.data
            user = request.user
            self.edit_password_logic.edit_password(data, user)

            return Response(None, HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)