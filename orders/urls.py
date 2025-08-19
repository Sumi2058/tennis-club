from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/create/<int:user_id>/<int:product_id>/', views.order_create, name='order_create'),
    path('orders/delete/<int:order_id>/', views.order_delete, name='order_delete'),
]
