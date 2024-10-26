# orders/urls.py
from django.urls import path,include
from .views import PlaceOrderView, OrderHistoryView, UpdateOrderStatusView

urlpatterns = [
    path('place/', PlaceOrderView.as_view(), name='place-order'),
    path('history/', OrderHistoryView.as_view(), name='order-history'),
    path('update/<int:id>/', UpdateOrderStatusView.as_view(), name='update-order-status'),
    


   

]