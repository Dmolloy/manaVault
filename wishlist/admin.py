from django.contrib import admin
from .models import WishlistItem


class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('card_name', 'user', 'desired_condition', 'max_price', 'created_at')
    list_filter = ('desired_condition', 'created_at')
    search_fields = ('card_name', 'set_name', 'user__username')


admin.site.register(WishlistItem, WishlistItemAdmin)