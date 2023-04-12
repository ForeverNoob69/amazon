from pyexpat import model
from rest_framework import serializers
from App.models import *
from django.contrib.auth.models import User


class productSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# class customerSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = '__all__'

class orderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class orderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class shippingAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'