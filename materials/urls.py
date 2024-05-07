from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.views import CourseViewSet, LessonListApiView, LessonCreateApiView, LessonRetrieveApiView, \
    LessonUpdateApiView, LessonDestroyApiView, SubscriptionApiView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name='lessons-list'),
    path("lessons/<int:pk>", LessonRetrieveApiView.as_view(), name='lessons-retrieve'),
    path("lessons/create/", LessonCreateApiView.as_view(), name='lessons-create'),
    path("lessons/<int:pk>/delete/", LessonDestroyApiView.as_view(), name='lessons-delete'),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name='lessons-update'),
    path("subscription/", SubscriptionApiView.as_view(), name='subscription-list'),
]

urlpatterns += router.urls
