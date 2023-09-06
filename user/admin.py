from django.contrib import admin
from user.models import User, UserAddress


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    This class will register user model in admin site.
    """
    list_display = ['username']


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    """
    This class will register user address in admin site.
    """
    list_display = ['address_type', 'address']
