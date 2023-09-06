from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    This class will register product model in admin site.
    """
    list_display = ['name', 'price', 'category']
