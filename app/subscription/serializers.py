from django.conf import settings
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from subscription import models
from user.models import User


class SubscriptionSerializer(serializers.ModelSerializer):
    cover_image = serializers.FileField(required=True)
    price = serializers.IntegerField(required=True, min_value=0)

    class Meta:
        model = models.Subscription
        fields = ['name', 'description', 'cover_image', 'price']
        read_only_fields = ['created_at']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.cover_image = validated_data.get('cover_image', instance.cover_image)
        instance.updated_at = timezone.now()
        instance.save()

    def validate(self, attrs):
        image_type = attrs.get('cover_image').content_type.split('/')[1]

        if image_type not in settings.AWS_ALLOWED_IMAGES_TYPE:
            raise ValidationError('Allowed image types are {}'.format(settings.AWS_ALLOWED_IMAGES_TYPE))
        return attrs

    def create(self, validated_data):
        self.Meta.model.objects.create(
            creator=self.context['request'].user,
            name=validated_data.get('name', None),
            description=validated_data.get('description', None),
            cover_image=validated_data.get('cover_image', None),
            price=validated_data.get('price', 0),
        )
        return validated_data



