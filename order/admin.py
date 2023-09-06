from django.contrib import admin
from order.models import Order, OrderInvoice


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    This class will register order model in admin site.
    """
    list_display = ['order', 'cart', 'user', 'status']


@admin.register(OrderInvoice)
class OrderInvoiceAdmin(admin.ModelAdmin):
    """
    This class will register order invoice model in admin site.
    """
    list_display = ['user', 'order', 'status']
