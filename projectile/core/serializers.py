from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from djoser.serializers import (
    UserCreateSerializer,
    PasswordResetConfirmSerializer,
)

from core.models import (
    User,
)


class MeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'title',
            'phone_number',

        )
        extra_kwargs = {'email': {'required': False}}

    def update(self, instance, validated_data):
        email = validated_data.pop('email', None)
        if email:
            if str(instance.email) == email:
                pass
            else:
                instance.pending_new_email = email

        is_boarded = validated_data.get('is_onboarded')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if is_boarded:
            if instance.check_onboarded_data_exists():
                pass
            else:
                raise serializers.ValidationError(
                    _('Missing required data for onboarding')
                )
        instance.save()
        return instance


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

        extra_kwargs = {
            'first_name': {'allow_blank': False},
            'last_name': {'allow_blank': False},
        }

    def update(self, instance, validated_data):
        raise NotImplementedError('This serializer does not support updates')

    def create(self, validated_data):
        user_serializer = UserCreateSerializer(data=validated_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        return user
