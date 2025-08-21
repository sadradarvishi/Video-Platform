from VideoProcessing.entity.video_entity import VideoEntity


class VideoUploadDao:


    def upload_video(
            self,
            title,
            creator,
            file,
            thumbnail,
    ):
        return VideoEntity.objects.create(
            title=title,
            creator=creator,
            file=file,
            thumbnail=thumbnail,
        )