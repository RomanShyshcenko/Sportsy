from django.contrib.auth import get_user_model
from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from user.models import Profile, password_regex

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'country',
                  'gender', 'birth_date')


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=False)
    is_verified = serializers.BooleanField()

    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number
        )
        instance.is_verified = False
        instance.save()

        return instance


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    phone_number = PhoneNumberSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'profile', 'phone_number']  # 'avatar',
        read_only_fields = ['id', 'email']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        # update profile data
        if profile_data and profile:
            profile.first_name = profile_data.get("first_name", profile.first_name)
            profile.last_name = profile_data.get("last_name", profile.last_name)
            profile.country = profile_data.get("country", profile.country)
            profile.gender = profile_data.get("gender", profile.gender)
            profile.birth_date = profile_data.get("birth_date", profile.birth_date)
            profile.save()

        return instance


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=120)
    password = serializers.CharField(max_length=55, validators=[password_regex], write_only=True)
    confirm_password = serializers.CharField(
        max_length=55, write_only=True,
        required=True
    )

    def validate_email(self, value):
        if value and User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User already exists!")
        return value

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Pleas confirm your password")
        return data

    def create(self, validated_data):

        user = User.objects.create_user(
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )

        return user


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, data):
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            return data
        raise serializers.ValidationError("This email doesn't exist!")


class ChangeForgottenPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        validators=[password_regex], max_length=55,
        write_only=True, required=True
    )
    confirm_password = serializers.CharField(
        validators=[password_regex], max_length=55,
        write_only=True, required=True
    )

    def validate(self, data):
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        if self.instance.verify_password(new_password):
            raise serializers.ValidationError('New password cannot match old.')

        elif new_password != confirm_password:
            raise serializers.ValidationError("Passwords doesn't match.")
        return data

    def update(self, instance, validated_data):
        new_password = validated_data.pop('new_password')
        instance.set_password(new_password)
        instance.save()

        return instance

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        max_length=55, write_only=True,
        required=True
    )
    new_password = serializers.CharField(
        validators=[password_regex], max_length=55,
        write_only=True, required=True
    )
    confirm_password = serializers.CharField(
        validators=[password_regex], max_length=55,
        write_only=True, required=True
    )

    def validate(self, data):
        new_password = data.get('new_password')

        if not self.instance.verify_password(data.get('old_password')):
            raise serializers.ValidationError('Pleas correctly enter your old password.')

        elif self.instance.verify_password(new_password):
            raise serializers.ValidationError('New password cannot match old.')

        elif new_password != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords doesn't match.")
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('new_password'))
        instance.save()
        return instance


class ChangeEmaiSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        email = data.get('email')

        if email == self.instance.email:
            raise serializers.ValidationError("New email can't math old.")

        return data

    def update(self, instance, validated_data):
        instance.email = validated_data.pop('email')
        instance.is_confirmed_email = False
        instance.save()
        return instance
