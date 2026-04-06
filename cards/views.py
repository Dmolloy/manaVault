from django.shortcuts import render
from .models import Card

# Create your views here.

def all_cards(request):
    cards = Card.objects.filter(is_active=True)
    return render(request, 'cards/cards.html', {'cards': cards})