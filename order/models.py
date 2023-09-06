from django.db import models
from django_extensions.db.models import TimeStampedModel
from cart.models import Cart
from user.models import User, UserAddress


class Order(TimeStampedModel):
    """
    This model will store order details.
    """
    STATUS = (
        ('Confirmed', 'Confirmed'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    )

    order = models.CharField(max_length=10, null=True, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myorders')
    total_amount = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS, default='Confirmed')
    delivery_address = models.ForeignKey(UserAddress, on_delete=models.SET_NULL, null=True,
                                         related_name='myaddress')

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
        return f"Order ID: {self.order} User ID: {self.user} Total amount: {self.total_amount}," \
               f" Order Status: {self.status}"


class OrderInvoice(TimeStampedModel):
    """
    This model will store order transaction detail.
    """
    STATUS = (
        ('Pending', 'Pending'),
        ('Successful', 'Successful'),
        ('Cancelled', 'Cancelled')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.IntegerField(null=True, blank=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_details')
    delivery_address = models.ForeignKey(UserAddress, on_delete=models.SET_NULL, null=True,
                                         related_name='delivery_address')
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')

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
        return f"User ID: {self.user} Order ID: {self.order} Status: {self.status}"
