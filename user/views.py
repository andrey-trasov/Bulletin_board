from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from user.models import User
from user.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """
    Регистрация пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)  # открываем для анонимных пользователей

    def perform_create(self, serializer):
        user = serializer.save()
        # user = serializer.save(commit=False)    # не сохраняем объект в бд
        user.set_password(user.password)    # хешируем пароль
        user.save()
