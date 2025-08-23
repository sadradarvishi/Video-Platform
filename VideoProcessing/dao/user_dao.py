from VideoProcessing.entity.user_entity import UserEntity
from typing import Optional

class UserDao:

    def get_user_by_id(self, id):
        return UserEntity.objects.get(id=id)

    def edit_user(
            self,
            user,
            first_name: Optional[str],
            last_name: Optional[str],
            phone_number: Optional[str],
            username: Optional[str],
            picture
    ):
        updates = {}

        if first_name is not None:
            updates['first_name'] = first_name

        if last_name is not None:
            updates['last_name'] = last_name

        if phone_number is not None:
            updates['phone_number'] = phone_number

        if username is not None:
            updates['username'] = username

        if picture is not None:
            updates['picture'] = picture

        # Update only the provided fields
        for field, value in updates.items():
            setattr(user, field, value)

        user.save(update_fields=updates.keys())
        return user

    def edit_password(self, password, user):
        user.password = password
        user.save()

        return user
