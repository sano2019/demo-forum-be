from django.conf import settings
from django.contrib.auth.tokens import default_token_generator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from djoser.utils import encode_uid

from core.models import User


class RemoveRegistrationAccount(APIView):
    """
    Removes the registration account so it can register again.
    """

    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        user = User.objects.filter(email=request.data['email'])
        if user.exists():
            user.first().delete()
        return Response()


class CreateTestAccount(APIView):
    """
    Creates a test account
    """

    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        is_active = request.data.pop('is_active', False)
        user = User.objects.create_user(email, password=password)

        if not is_active:
            user.is_active = False
            user.save(update_fields=['is_active'])

        return Response(
            {
                'data': {
                    'activationUrl': settings.DJOSER['ACTIVATION_URL'].format(
                        uid=encode_uid(user.pk),
                        token=default_token_generator.make_token(user),
                    )
                }
            }
        )


class ResetPasswordLink(APIView):
    """
    Creates and responds with a reset password link for the user.
    """

    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        email = request.data['email']
        user = User.objects.get(email=email)

        return Response(
            {
                'data': {
                    'resetPasswordUrl': settings.DJOSER[
                        'PASSWORD_RESET_CONFIRM_URL'
                    ].format(
                        email=user.email,
                        uid=encode_uid(user.pk),
                        token=default_token_generator.make_token(user),
                    )
                }
            }
        )
