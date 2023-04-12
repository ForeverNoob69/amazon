from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



from App.models import *
from api.forms import RegisterForm
from .serializers import *
from django.contrib.auth.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET','POST'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/refresh',
    ]
    return Response(routes)

@api_view(['POST'])
def getUserData(request):
    if request.method == 'POST':
        
        # serializer = userSerializers(data={"username":request.data['username'],"email":request.data["email"],"password":make_password(request.data['password'])})
        # if serializer.is_valid():
        #     serializer.save()
        user = User.objects.create_user(username=request.data['username'],password=request.data['password'],email=request.data['email'])
        print("user:",user)
        serializer = userSerializers(user)
        username = request.data['username']
        email = request.data['email']
        user = User.objects.get(id=user.id)
        # form = Customer.objects.create(name=username,email=email,user=user)
    if request.method == 'GET':
        user = User.objects.all()
        serializer = userSerializers(user,many=True)
    return Response(serializer.data)

# @api_view(['GET','POST'])
# def getCustomerData(request):
#     if request.method=='GET':
#         customer = Customer.objects.all()
#         serializers = customerSerializers(customer,many=True)
#         return Response(serializers.data)
#     if request.method=='POST':
#         serializers = customerSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#         return Response(serializers.data)
    
@api_view(['GET'])
def getProductData(request):
    item = Product.objects.all()
    serializer = productSerializers(item,many=True)
    
    return Response(serializer.data)

@api_view(['GET','POST'])
def getOrderData(request):
    if request.method == 'GET':
        item = Order.objects.all()
        serializer = orderSerializers(item,many=True)
    if request.method == 'POST':
        serializer = orderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)

@api_view(['GET','POST'])
def getOrderItemData(request):
    if request.method=='GET':
        item = OrderItem.objects.all()
        serializer = orderItemSerializers(item,many=True)
    if request.method=='POST':
        print(request.data)
        serializer = orderItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)

@api_view(['GET','POST'])
def getShippingAddressData(request):
    if request.method == 'GET':
        item = ShippingAddress.objects.all()
        serializer = shippingAddressSerializers(item,many=True)
    if request.method == 'POST':
        serializer = shippingAddressSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)

