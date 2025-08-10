from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated

from VideoProcessing.logic.video_upload_logic import VideoUploadLogic

class VideoUploadController(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_upload_logic = VideoUploadLogic()

    def post(self, request):
        try:
            data = request.data
            creator = request.user
            self.video_upload_logic.upload_video(data, creator)

            return Response(None, HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)