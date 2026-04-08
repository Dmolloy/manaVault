from django.urls import path
from .views import view_cart, add_to_cart, update_cart, remove_from_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<int:card_id>/', add_to_cart, name='add_to_cart'),
    path('update/<int:card_id>/', update_cart, name='update_cart'),
    path('remove/<int:card_id>/', remove_from_cart, name='remove_from_cart'),
]