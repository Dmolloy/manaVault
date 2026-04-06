from django.shortcuts import render, get_object_or_404
from .models import Card

# Create your views here.

def all_cards(request):
    cards = Card.objects.filter(is_active=True)
    return render(request, 'cards/cards.html', {'cards': cards})


def card_detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id, is_active=True)
    return render(request, 'cards/card_detail.html', {'card': card})