from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from VideoProcessing.logic.video_logic import VideoLogic
from VideoProcessing.serializer.video_serializer import VideoSerializer

class VideoController(APIView, LimitOffsetPagination):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_logic = VideoLogic()

    def get(self, request):
        try:
            data = request.query_params
            title = data.get('title')

            if title:
                query_data = self.video_logic.get_video_by_title(title)
                paginated_data = self.paginate_queryset(query_data, request, view=self)
                serialized_data = VideoSerializer(paginated_data, many=True)

                return Response(serialized_data.data, HTTP_200_OK)

            query_data = self.video_logic.get_all_videos()
            paginated_data = self.paginate_queryset(query_data, request, view=self)
            serialized_data = VideoSerializer(paginated_data, many=True)

            return Response(serialized_data.data, HTTP_200_OK)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)
