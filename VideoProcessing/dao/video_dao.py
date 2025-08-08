from VideoProcessing.entity.video_entity import VideoEntity

class VideoDao:

    def get_all_videos(self):
        return VideoEntity.objects.all()

    def get_video_by_title(self, title):
        return VideoEntity.objects.filter(title__icontains = title).order_by('-uploaded_at')