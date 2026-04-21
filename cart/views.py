from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from cards.models import Card
from django.http import JsonResponse


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

    current_quantity = cart.get(str(card_id), 0)
    new_quantity = current_quantity + quantity

    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

    if new_quantity > card.stock_quantity:
        if is_ajax:
            return JsonResponse({
                'success': False,
                'message': f'You can only add up to {card.stock_quantity} of {card.name}.'
            })

        messages.error(request, f'You can only add up to {card.stock_quantity} of {card.name}.')
        return redirect('card_detail', card_id=card.id)

    cart[str(card_id)] = new_quantity
    request.session['cart'] = cart

    if is_ajax:
        return JsonResponse({
            'success': True,
            'message': f'{quantity} x {card.name} added to cart.'
        })

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