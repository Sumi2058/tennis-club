from django.urls import path
from . import views

urlpatterns = [
    path('product', views.product_list, name='product_list'),
    path('product/create', views.product_create, name='product_create'),
    
]
