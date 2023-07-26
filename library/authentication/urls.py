from django.urls import path, include
from . import views
from rest_framework import routers
from .views import CustomUserViewSet

router = routers.DefaultRouter()
router.register(r'user', CustomUserViewSet)

urlpatterns = [
    path("authentication/register", views.register, name="register"),
    path("authentication/login_user", views.login_user, name="login_user"),
    path("authentication/logout_user", views.logout_user, name="logout_user"),

    path('api/v1/user/', CustomUserViewSet.as_view({'get': 'list', 'post': 'create'}), name='all_users'),
    path('api/v1/user/<int:pk>', CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user_detail'),

]