from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentListApiView, PaymentCreateApiView, PaymentDestroyApiView, PaymentUpdateApiView, \
    PaymentRetrieveApiView, UserCreateApiView, UserListApiView

app_name = UsersConfig.name

urlpatterns = [
    path('payments/', PaymentListApiView.as_view(), name='payment_list'),
    path('payments/create/', PaymentCreateApiView.as_view(), name='payment_list'),
    path("payments/<int:pk>/delete/", PaymentDestroyApiView.as_view(), name='payment_delete'),
    path("payments/<int:pk>/update/", PaymentUpdateApiView.as_view(), name='payment_update'),
    path("payments/<int:pk>", PaymentRetrieveApiView.as_view(), name='payment_retrieve'),

    path('register/', UserCreateApiView.as_view(permission_classes=(AllowAny,)), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserListApiView.as_view(), name='user_list'),
]
