from django.urls import path, include
from author import views
from rest_framework import routers
from .views import AuthorViewSet

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('authors/create/', views.author_create, name='author_create'),
    path('authors/delete/<int:author_id>/', views.author_delete, name='author_delete'),

    path('api/v1/author/', AuthorViewSet.as_view({'get': 'list', 'post': 'create'}), name='author_all'),
    path('api/v1/author/<int:pk>', AuthorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='author_detail'),
]
