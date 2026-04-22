from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import ContactForm


def index(request):
    return HttpResponse("ManaVault homepage works")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Message sent successfully.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})