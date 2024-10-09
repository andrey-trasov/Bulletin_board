from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        password = attrs.get("password")  # достаем пароль
        attrs["password"] = make_password(password)  # хешируем и сохраняем его
        return attrs
