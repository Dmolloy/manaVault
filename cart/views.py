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

    messages.success(request, f'{quantity} x {card.name} added to your cart.')
    return redirect('card_detail', card_id=card.id)

def update_cart(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    if quantity > card.stock_quantity:
        messages.error(request, f'Only {card.stock_quantity} of {card.name} available.')
        return redirect('view_cart')

    if quantity > 0:
        cart[str(card_id)] = quantity
        messages.success(request, f'Updated {card.name} quantity to {quantity}.')
    else:
        cart.pop(str(card_id), None)
        messages.success(request, f'{card.name} removed from your cart.')

    request.session['cart'] = cart
    return redirect('view_cart')


def remove_from_cart(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    cart = request.session.get('cart', {})

    if str(card_id) in cart:
        cart.pop(str(card_id))
        request.session['cart'] = cart
        messages.success(request, f'{card.name} removed from your cart.')

    return redirect('view_cart')