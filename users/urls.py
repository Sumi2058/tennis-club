from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('user/create/', views.user_create, name='user_create'),
    path('user/login/', views.user_login, name='user_login'),
    path('user/<int:pk>/update/', views.user_update, name='user_update'),
    path('user/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
