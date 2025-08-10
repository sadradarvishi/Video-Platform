from VideoProcessing.dao.video_upload_dao import VideoUploadDao


class VideoUploadLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_upload_dao = VideoUploadDao()

    def upload_video(self, data, creator):
        title = data.get('title')
        file = data.get('file')
        thumbnail = data.get('thumbnail')

        return self.video_upload_dao.upload_video(
            title=title,
            creator=creator,
            file=file ,
            thumbnail=thumbnail
        )
