from django.urls import path
from .views import all_cards, card_detail

urlpatterns = [
    path('', all_cards, name='cards'),
    path('<int:card_id>/', card_detail, name='card_detail'),
]