from django.urls import path
from . import views
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.getRoutes,name='get_routes'),
    path('get-product-data/',views.getProductData,name='getProductData'),
    # path('get-customer-data/',views.getCustomerData,name='getCustomerData'),
    path('get-user-data/',views.getUserData,name='getUserData'),

    path('get-order-data/',views.getOrderData,name='getOrderData'),
    path('get-order-item-data/',views.getOrderItemData,name='getOrderItemData'),
    path('get-shipping-address-data/',views.getShippingAddressData,name='getShippingAddressData'),


    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
