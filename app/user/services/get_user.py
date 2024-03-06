from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

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

    @staticmethod
    def get_user_by_email(email: str):
        user = get_object_or_404(User, email=email)
