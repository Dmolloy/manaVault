from django.urls import path
from .views import register, profile, order_detail

urlpatterns = [
    path('register/', register, name='register'),
    path('', profile, name='profile'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
]