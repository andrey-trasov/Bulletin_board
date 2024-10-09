from django.urls import path
from rest_framework.permissions import AllowAny

from announcement.apps import AnnouncementConfig
from announcement.views import (
    AnnouncementCreateApiView,
    AnnouncementListApiView,
    AnnouncementRetrieveApiView,
    AnnouncementDestroyApiView,
    AnnouncementUpdateApiView,
    FeedbackCreateApiView,
    FeedbackListApiView,
    FeedbackRetrieveApiView,
    FeedbackDestroyApiView,
    FeedbackUpdateApiView,
)

app_name = AnnouncementConfig.name

urlpatterns = [
    path(
        "announcement_create/",
        AnnouncementCreateApiView.as_view(),
        name="announcement_create",
    ),
    path(
        "announcement/",
        AnnouncementListApiView.as_view(permission_classes=(AllowAny,)),
        name="announcement_list",
    ),
    path(
        "announcement/<int:pk>/",
        AnnouncementRetrieveApiView.as_view(),
        name="announcement_retrieve",
    ),
    path(
        "announcement_destroy/<int:pk>/",
        AnnouncementDestroyApiView.as_view(),
        name="announcement_destroy",
    ),
    path(
        "announcement_update/<int:pk>/",
        AnnouncementUpdateApiView.as_view(),
        name="announcement_update",
    ),
    path("feedback_create/", FeedbackCreateApiView.as_view(), name="feedback_create"),
    path("feedback/", FeedbackListApiView.as_view(), name="feedback_list"),
    path(
        "feedback/<int:pk>/",
        FeedbackRetrieveApiView.as_view(),
        name="feedback_retrieve",
    ),
    path(
        "feedback_destroy/<int:pk>/",
        FeedbackDestroyApiView.as_view(),
        name="feedback_destroy",
    ),
    path(
        "feedback_update/<int:pk>/",
        FeedbackUpdateApiView.as_view(),
        name="feedback_update",
    ),
]
