import uuid

from django.contrib.auth import get_user_model

User = get_user_model()


class GetUserService:
    @staticmethod
    def get_user_by_uuid(user_uuid: str) -> dict:
        """Get user with all related personal info."""
        user = User.objects.select_related('profile', 'phone').get(id=user_uuid)
        profile = user.profile
        phone_number = user.phone

        return {
            "id": user.id,
            "email": user.email,
            "is_confirmed_email": user.is_confirmed_email,
            "profile_info": profile,
            "phone_number": phone_number
        }
