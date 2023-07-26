from rest_framework import serializers
from .models import Order
from authentication.serializers import CustomUserSerializer
from book.serializers import BookSerializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
