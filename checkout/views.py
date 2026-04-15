import stripe
from django.conf import settings
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

    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        checkout_data = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'country': request.POST.get('country'),
            'postcode': request.POST.get('postcode'),
            'town_or_city': request.POST.get('town_or_city'),
            'street_address1': request.POST.get('street_address1'),
            'street_address2': request.POST.get('street_address2'),
            'county': request.POST.get('county'),
        }

        request.session['checkout_data'] = checkout_data

        line_items = []

        for item in cart_items:
            line_items.append({
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': item['card'].name,
                    },
                    'unit_amount': int(item['card'].price * 100),
                },
                'quantity': item['quantity'],
            })

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri('/checkout/success/'),
            cancel_url=request.build_absolute_uri('/cart/'),
        )

        return redirect(session.url, code=303)

    return render(request, 'checkout/checkout.html', {
        'cart_items': cart_items,
        'total': total,
    })


def checkout_success(request):
    cart = request.session.get('cart', {})
    checkout_data = request.session.get('checkout_data')

    if not cart or not checkout_data:
        messages.error(request, "No completed checkout data found.")
        return redirect('cards')

    cart_items = []
    total = Decimal('0.00')

    for card_id, quantity in cart.items():
        card = get_object_or_404(Card, pk=card_id, is_active=True)

        if quantity > card.stock_quantity:
            messages.error(request, f"Only {card.stock_quantity} of {card.name} available.")
            return redirect('view_cart')

        subtotal = card.price * quantity
        total += subtotal
        cart_items.append({
            'card': card,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    order = Order.objects.create(
        user=request.user if request.user.is_authenticated else None,
        full_name=checkout_data.get('full_name'),
        email=checkout_data.get('email'),
        phone_number=checkout_data.get('phone_number'),
        country=checkout_data.get('country'),
        postcode=checkout_data.get('postcode'),
        town_or_city=checkout_data.get('town_or_city'),
        street_address1=checkout_data.get('street_address1'),
        street_address2=checkout_data.get('street_address2'),
        county=checkout_data.get('county'),
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
    request.session['checkout_data'] = {}

    messages.success(request, "Payment successful. Your order has been created.")
    return render(request, 'checkout/checkout_success.html', {'order': order})