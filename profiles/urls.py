from django.urls import path
from .views import profile, order_detail

urlpatterns = [
    path('', profile, name='profile'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
]