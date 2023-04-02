from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from .models import User


class CustomLoginSerializer(LoginSerializer):
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})
    username = None

    def get_auth_user_using_orm(self, username, email, password):
        if email:
            try:
                username = User.objects.get(email__iexact=email).get_username()
            except User.DoesNotExist:
                pass

        if username:
            return self._validate_username_email(username, '', password)

        return None
