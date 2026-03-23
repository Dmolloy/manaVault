from django.contrib import admin
from .models import Card

# Register your models here.
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'set_name',
        'rarity',
        'condition',
        'price',
        'stock_quantity',
        'is_active',
    )
    list_filter = ('rarity', 'condition', 'is_active', 'set_name')
    search_fields = ('name', 'set_name', 'card_type')