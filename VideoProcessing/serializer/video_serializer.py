from rest_framework import serializers

from VideoProcessing.entity.video_entity import VideoEntity

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoEntity
        fields = '__all__'