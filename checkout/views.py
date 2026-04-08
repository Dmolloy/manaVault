from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order, OrderLineItem
from cards.models import Card


def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect('cards')

    if request.method == 'POST':
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
        )

        total = 0

        for card_id, quantity in cart.items():
            card = Card.objects.get(id=card_id)
            lineitem = OrderLineItem.objects.create(
                order=order,
                card=card,
                quantity=quantity,
            )
            total += lineitem.lineitem_total

        order.order_total = total
        order.save()

        request.session['cart'] = {}

        messages.success(request, "Order placed successfully!")
        return redirect('home')

    return render(request, 'checkout/checkout.html')