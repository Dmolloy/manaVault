from django.shortcuts import render, redirect
from django.contrib import messages
from cards.models import Card
from .forms import ContactForm


def index(request):
    featured_cards = Card.objects.filter(is_active=True)[:3]
    return render(request, 'home/index.html', {
        'featured_cards': featured_cards,
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thanks for your message. We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})