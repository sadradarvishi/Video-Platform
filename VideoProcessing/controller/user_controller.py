from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated

from VideoProcessing.logic.user_logic import UserLogic
from VideoProcessing.serializer.user_serializer import UserSerializer

class UserController(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_logic = UserLogic()

    def get(self, request):
        try:
            user = request.user
            id = user.id
            data = self.user_logic.get_user_by_id(id)
            serialized_data = UserSerializer(data)

            return Response(serialized_data.data, HTTP_200_OK)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)
