from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemInline,)
    list_display = ('id', 'full_name', 'email', 'date', 'order_total')
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem)