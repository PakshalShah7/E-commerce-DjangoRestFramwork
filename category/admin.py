from django.contrib import admin
from category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    This class will register category model in admin site.
    """
    list_display = ['name']
