from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from cards.models import Card

from .forms import WishlistItemForm
from .models import WishlistItem


@login_required
def wishlist(request):
    items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {
        'items': items,
    })


@login_required
def add_wishlist_item(request):
    if request.method == 'POST':
        form = WishlistItemForm(request.POST)
        if form.is_valid():
            wishlist_item = form.save(commit=False)
            wishlist_item.user = request.user
            wishlist_item.save()
            messages.success(request, 'Wishlist item added successfully.')
            return redirect('wishlist')
    else:
        form = WishlistItemForm()

    return render(request, 'wishlist/wishlist_form.html', {
        'form': form,
        'page_title': 'Add Wishlist Item',
        'button_text': 'Add Item',
    })


@login_required
def edit_wishlist_item(request, item_id):
    wishlist_item = get_object_or_404(
        WishlistItem,
        id=item_id,
        user=request.user
    )

    if request.method == 'POST':
        form = WishlistItemForm(request.POST, instance=wishlist_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wishlist item updated successfully.')
            return redirect('wishlist')
    else:
        form = WishlistItemForm(instance=wishlist_item)

    return render(request, 'wishlist/wishlist_form.html', {
        'form': form,
        'page_title': 'Edit Wishlist Item',
        'button_text': 'Update Item',
    })


@login_required
def delete_wishlist_item(request, item_id):
    wishlist_item = get_object_or_404(
        WishlistItem,
        id=item_id,
        user=request.user
    )

    if request.method == 'POST':
        wishlist_item.delete()
        messages.success(request, 'Wishlist item deleted successfully.')
        return redirect('wishlist')

    return render(request, 'wishlist/wishlist_confirm_delete.html', {
        'wishlist_item': wishlist_item,
    })

@login_required
def add_existing_card_to_wishlist(request, card_id):
    card = get_object_or_404(Card, id=card_id)

    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user,
        card_name=card.name,
        set_name=card.set_name,
        defaults={
            'desired_condition': 'any',
            'max_price': card.price,
            'notes': 'Added from ManaVault card listing.',
        }
    )

    if created:
        messages.success(request, f'{card.name} was added to your wishlist.')
    else:
        messages.info(request, f'{card.name} is already in your wishlist.')

    return redirect('card_detail', card_id=card.id)