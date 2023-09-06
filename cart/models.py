from django.db import models
from django_extensions.db.models import TimeStampedModel
from product.models import Product
from user.models import User


class Cart(TimeStampedModel):
    """
    This model will store cart details.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mycart')
    status = models.BooleanField(default=True)

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        ordering = ['id']

    def __str__(self):
        """
        The method allows us to convert an object into a string representation.
        """
        return f"Cart: {self.id} User: {self.user}"

    @property
    def set_total(self):
        """
        This method will calculate total cost of cart items.
        """
        total = 0
        for item in self.carts.all():
            total += item.sub_total()
        return total


class CartItem(TimeStampedModel):
    """
    This model will store cart item details
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, related_name='carts')
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='selected_items')
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        ordering = ['id']

    def __str__(self):
        """
        The method allows us to convert an object into a string representation.
        """
        return f"ID: {self.id}, Cart_ID: {self.cart}, Product: {self.item}, Quantity: {self.quantity}"

    def sub_total(self):
        """
        This method will calculate sub-total of selected product.
        """
        return self.quantity * self.item.price
