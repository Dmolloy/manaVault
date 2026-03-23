from django.shortcuts import render
from cards.models import Card


def index(request):
    featured_cards = Card.objects.filter(is_active=True)[:3]
    return render(request, 'home/index.html', {
        'featured_cards': featured_cards,
    })