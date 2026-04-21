from django.shortcuts import render, get_object_or_404
from .models import Card


def all_cards(request):
    cards = Card.objects.filter(is_active=True)
    selected_type = request.GET.get('type')

    if selected_type:
        cards = cards.filter(card_type__iexact=selected_type)

    card_types = (
        Card.objects.filter(is_active=True)
        .values_list('card_type', flat=True)
        .distinct()
        .order_by('card_type')
    )

    return render(request, 'cards/cards.html', {
        'cards': cards,
        'card_types': card_types,
        'selected_type': selected_type,
    })


def card_detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id, is_active=True)
    return render(request, 'cards/card_detail.html', {'card': card})