from VideoProcessing.dao.user_dao import UserDao


class UserLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_dao = UserDao()

    def get_user_by_id(self, id):
        return self.user_dao.get_user_by_id(id=id)
