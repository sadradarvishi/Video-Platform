from VideoProcessing.dao.video_dao import VideoDao

class VideoLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_dao = VideoDao()

    def get_all_videos(self):
        return self.video_dao.get_all_videos()

    def get_video_by_title(self, title):
        return self.video_dao.get_video_by_title(title=title)

