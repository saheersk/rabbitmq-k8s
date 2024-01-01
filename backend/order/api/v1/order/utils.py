import json

import pika
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from api.v1.order.producer import authenticate_user


class CustomTokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_token = request.META.get('HTTP_AUTHORIZATION')

        print(auth_token, "None")

        user_token = {
            'token': auth_token
        }

        if not user_token:
            return None

        user = authenticate_user(user_token)

        if not user:
            raise AuthenticationFailed('Invalid authentication token')

        return (user, None)
