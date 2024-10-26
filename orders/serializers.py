# orders/serializers.py
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '_all_'
        read_only_fields = ['user', 'status', 'payment_status']