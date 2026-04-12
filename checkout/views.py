from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderLineItem
from cards.models import Card


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect('cards')

    cart_items = []
    total = Decimal('0.00')

    for card_id, quantity in cart.items():
        card = get_object_or_404(Card, pk=card_id, is_active=True)
        subtotal = card.price * quantity
        total += subtotal
        cart_items.append({
            'card': card,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    if request.method == 'POST':
        for item in cart_items:
            if item['quantity'] > item['card'].stock_quantity:
                messages.error(
                    request,
                    f"Only {item['card'].stock_quantity} of {item['card'].name} available."
                )
                return redirect('view_cart')

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number'),
            country=request.POST.get('country'),
            postcode=request.POST.get('postcode'),
            town_or_city=request.POST.get('town_or_city'),
            street_address1=request.POST.get('street_address1'),
            street_address2=request.POST.get('street_address2'),
            county=request.POST.get('county'),
            order_total=total,
        )

        for item in cart_items:
            OrderLineItem.objects.create(
                order=order,
                card=item['card'],
                quantity=item['quantity'],
            )
            item['card'].stock_quantity -= item['quantity']
            item['card'].save()

        request.session['cart'] = {}
        messages.success(request, "Order placed successfully.")
        return redirect('checkout_success', order_id=order.id)

    return render(request, 'checkout/checkout.html', {
        'cart_items': cart_items,
        'total': total,
    })


def checkout_success(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'checkout/checkout_success.html', {'order': order})