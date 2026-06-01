from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

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