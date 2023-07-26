from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)

urlpatterns = [
    path("books/", views.index_book, name="index_books"),
    path("ubooks/book/<str:book_id>", views.book_by_id, name="book_by_id"),
    path("books/filter/", views.filter_by, name="filter_by_page"),
    path("books/provided-to/", views.provided_to, name="provided_to"),
    path("books/create-book/", views.create_book, name="create_book"),
    path("books/create-book_in_db/", views.create_book_in_db, name="create_book_in_db"),
    path("books/delte-book/<str:book_id>", views.delete_book, name="delete_book"),

    path('api/v1/book/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='book_all'),
    path('api/v1/book/<int:pk>', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book_detail'),
]