from django import forms
from .models import WishlistItem


class WishlistItemForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = [
            'card_name',
            'set_name',
            'desired_condition',
            'max_price',
            'notes',
        ]
        widgets = {
            'card_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Card name'
            }),
            'set_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Set name (optional)'
            }),
            'desired_condition': forms.Select(attrs={
                'class': 'form-select'
            }),
            'max_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Maximum price'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Notes about this card'
            }),
        }