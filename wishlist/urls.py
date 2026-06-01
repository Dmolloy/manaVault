from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add/', views.add_wishlist_item, name='add_wishlist_item'),
    path('edit/<int:item_id>/', views.edit_wishlist_item, name='edit_wishlist_item'),
    path('delete/<int:item_id>/', views.delete_wishlist_item, name='delete_wishlist_item'),
    path('add-card/<int:card_id>/', views.add_existing_card_to_wishlist, name='add_existing_card_to_wishlist'),
]