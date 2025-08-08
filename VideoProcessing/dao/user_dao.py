from VideoProcessing.entity.user_entity import UserEntity

class UserDao:

    def get_user_by_id(self, id):
        return UserEntity.objects.get(id=id)
