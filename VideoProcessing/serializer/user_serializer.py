from rest_framework import serializers

from VideoProcessing.entity.user_entity import UserEntity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntity
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'username',
            'picture',
            'join_date',
        ]