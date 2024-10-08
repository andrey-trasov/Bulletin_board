from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from announcement.models import Announcement, Feedback
from announcement.paginators import CustomPagination
from announcement.permissions import IsOwner, IsAdmin
from announcement.serializers import AnnouncementSerializer, FeedbackSerializer


# объявления
class AnnouncementCreateApiView(CreateAPIView):
    """
    Создание нового объявления.
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = (IsAuthenticated,)  # только для авторизованных пользователей

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)    #присваиваем создателя к объявлению

class AnnouncementListApiView(ListAPIView):
    """
    Список всех объявлений с пагинацией.
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    pagination_class = CustomPagination    # пагинация
    permission_classes = (AllowAny,)  # открываем для анонимных пользователей

    # фильтрация товаров по названию
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('title',)

class AnnouncementRetrieveApiView(RetrieveAPIView):
    """
    Получение детального описания одного объявления.
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = (IsAuthenticated,)

class AnnouncementDestroyApiView(DestroyAPIView):
    """
    Удаление объявления.
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin)


class AnnouncementUpdateApiView(UpdateAPIView):
    """
    Редактирование объявления.
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin)


# отзывы
class FeedbackCreateApiView(CreateAPIView):
    """
    Создание нового отзыва.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)    #присваиваем создателя к комментарию


class FeedbackListApiView(ListAPIView):
    """
    Список всех отзывов.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)


class FeedbackRetrieveApiView(RetrieveAPIView):
    """
    Получение детального описания одного отзыва.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackDestroyApiView(DestroyAPIView):
    """
    Удаление отзыва.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin)


class FeedbackUpdateApiView(UpdateAPIView):
    """
    Редактирование отзыва.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsAdmin)

