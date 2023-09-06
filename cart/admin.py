from django.contrib import admin
from cart.models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    This class will register cart model in admin site.
    """
    list_display = ['user', 'status']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    This class will register cart item model in admin site.
    """
    list_display = ['cart', 'item', 'quantity']
