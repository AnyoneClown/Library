from django.urls import path, include
from . import views
from rest_framework import routers
from .views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)


urlpatterns = [
    path("orders/", views.index_order, name="index_order"),
    path("orders/all-orders", views.all_orders, name="all_orders"),
    path("orders/user-orders/<int:user_id>", views.user_orders, name="user_orders"),
    path("orders/delete/<int:order_id>", views.delete_order, name="delete_order"),
    path("orders/mark-as-returned/<int:order_id>", views.mark_as_returned, name="mark_as_returned"),
    path("orders/create-order", views.create_order, name="create_order"),
    path("orders/place-order", views.place_order, name="place_order"),

    path('api/v1/order/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='all_orders'),
    path('api/v1/order/<int:pk>', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='order_detail'),

    path('api/v1/user/<int:user_id>/order/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='orders'),
    path('api/v1/user/<int:user_id>/order/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='order_list'),
]