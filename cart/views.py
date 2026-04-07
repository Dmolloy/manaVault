from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from cards.models import Card


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for card_id, quantity in cart.items():
        card = get_object_or_404(Card, pk=card_id)
        subtotal = quantity * card.price
        total += subtotal

        cart_items.append({
            'card': card,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })

def add_to_cart(request, card_id):
    card = get_object_or_404(Card, pk=card_id)

    quantity = int(request.POST.get('quantity', 1))

    cart = request.session.get('cart', {})

    if str(card_id) in cart:
        cart[str(card_id)] += quantity
    else:
        cart[str(card_id)] = quantity

    request.session['cart'] = cart

    messages.success(request, f'Added {card.name} to your cart')

    return redirect('card_detail', card_id=card.id)