from VideoProcessing.entity.video_entity import VideoEntity

class VideoDao:

    def get_all_videos(self):
        return VideoEntity.objects.filter(status='completed').order_by('-uploaded_at')

    def get_video_by_title(self, title):
        return VideoEntity.objects.filter(
            title__icontains=title,
            status='completed'
        ).order_by('-uploaded_at')