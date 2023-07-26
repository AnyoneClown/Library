from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.models import CustomUser
from order.models import Order
from book.models import Book
import datetime
from django.utils import timezone


from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from .serializers import *

@permission_classes([IsAdminUser])
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def index_order(request):
    user = request.user
    if user.is_authenticated:
        context = {"user":user, "orders_active": "active"}
        return render(request, 'index_order.html', context=context)
    else:
        return HttpResponse("<h1>Not logged in</h1>")
    
def user_orders(request, user_id):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    if user.id != user_id and user.role != 1:
        return HttpResponse("<h1>You can't view this user's orders</h1>")
    orders = Order.objects.filter(user_id=user_id)
    book_names = [Book.objects.get(id=order.book_id).name for order in orders]
    zipped_data = list(zip(orders, book_names))
    context = {"orders": zipped_data, "orders_active": "active"}
    return render(request, "user_orders.html", context=context)
    
def create_order(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")  
    context = {"books": Book.objects.all(), "orders_active": "active"}
    return render(request, "create_order.html", context=context)

def all_orders(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    if user.role != 1:
        return HttpResponse("<h1>Only admins are allowed</h1>")
    context = {"orders": Order.objects.all(), "orders_active": "active"}
    return render(request, 'all_orders.html', context=context)
    
def delete_order(request, order_id):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    if user.role != 1:
        return HttpResponse("<h1>Only admins are allowed</h1>")
    Order.delete_by_id(order_id)
    return redirect("all_orders")
          
    

def place_order(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    user = CustomUser.objects.get(id=request.user.id)
    book = Book.objects.filter(id = request.POST["book_id"]).first()
    if book.count < 1:
        return HttpResponse("<h1>These books are out of stock</h1>")
    book.count -= 1
    book.save()
    future_date = int(request.POST["return_date"])
    timestamp = timezone.now() + datetime.timedelta(future_date)
    Order.create(user, book, timestamp)  
    return redirect("user_orders", user_id=user.id)

def mark_as_returned(request, order_id):
    order = Order.get_by_id(order_id)
    order.book.count += 1
    order.book.save()
    order.end_at = timezone.now()
    order.save()
    return redirect("all_orders")