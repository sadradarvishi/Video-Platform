from VideoProcessing.entity.user_entity import UserEntity

class LoginDao:

    def get_user_by_username(self, username):
        return UserEntity.objects.get(username=username)