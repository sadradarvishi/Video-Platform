from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated

from VideoProcessing.logic.edit_user_logic import EditUserLogic

class EditUserController(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.edit_user_logic = EditUserLogic()


    def patch(self, request):
        try:
            data = request.data
            picture = request.FILES
            user = request.user

            self.edit_user_logic.edit_profile(data, user, picture)

            return Response(None, HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)