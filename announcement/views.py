from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView

from announcement.models import Announcement, Feedback
from announcement.serializers import AnnouncementSerializer, FeedbackSerializer


# объявления
class AnnouncementCreateApiView(CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)    #присваиваем создателя к объявлению

class AnnouncementListApiView(ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    # abkmnhfwbz
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('title',)

class AnnouncementRetrieveApiView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementDestroyApiView(DestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementUpdateApiView(UpdateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


# отзывы
class FeedbackCreateApiView(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)    #присваиваем создателя к комментарию


class FeedbackListApiView(ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackRetrieveApiView(RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackDestroyApiView(DestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackUpdateApiView(UpdateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

