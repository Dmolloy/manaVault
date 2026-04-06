from django.urls import path
from .views import all_cards

urlpatterns = [
    path('', all_cards, name='cards'),
]