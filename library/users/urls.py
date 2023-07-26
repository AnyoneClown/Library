from django.urls import path
from . import views


urlpatterns = [
    path("users/", views.index_users, name="index_users"),
    path("users/all-users", views.all_users, name="all_users"),
    path("users/user/<int:user_id>", views.user_by_id, name="user_by_id"),
    path("users/update-user/<int:user_id>", views.update_user, name="update_user"),
    path("users/delete-user/<int:user_id>", views.delete_user, name="delete_user"),
    path("users/update-password/<int:user_id>", views.update_password, name="update_password"),
]