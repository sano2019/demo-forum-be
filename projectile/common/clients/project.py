from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings

from core.tests.factories import UserFactory


class ProjectClient:
    CLIENT = None
    SUPERUSER = None
    RESPONSE = None

    def __init__(self):
        self.create()
        # self.authenticate_user(self.USER)

    def create(self):
        self.CLIENT = APIClient()
        # self.USER = UserFactory.create_dummy()

    # Authentication
    def authenticate_user(self, user):
        token = self.get_token_for_user(user)
        jwt_token = self.get_formatted_token(token)
        self.CLIENT.credentials(HTTP_AUTHORIZATION=jwt_token)

    def get_token_for_user(self, user):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def get_formatted_token(self, token):
        return 'Bearer {}'.format(token)

    # Requests
    def do_get(self, url, payload=None, format='json'):
        self.RESPONSE = self.CLIENT.get(url, payload, format=format)
        if hasattr(self.RESPONSE, 'data'):
            return self.RESPONSE.data

    def do_post(self, url, payload=None, format='json'):
        self.RESPONSE = self.CLIENT.post(url, payload, format=format)
        if hasattr(self.RESPONSE, 'data'):
            return self.RESPONSE.data

    def do_put(self, url, payload=None, format='json'):
        self.RESPONSE = self.CLIENT.put(url, payload, format=format)
        if hasattr(self.RESPONSE, 'data'):
            return self.RESPONSE.data

    def do_patch(self, url, payload=None, format='json'):
        self.RESPONSE = self.CLIENT.patch(url, payload, format=format)
        if hasattr(self.RESPONSE, 'data'):
            return self.RESPONSE.data

    def do_delete(self, url, payload=None, format='json'):
        self.RESPONSE = self.CLIENT.delete(url, payload, format=format)
        if hasattr(self.RESPONSE, 'data'):
            return self.RESPONSE.data
