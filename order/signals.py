""" This file contains signal for order model which is used in project. """

from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Order


@receiver(post_save, sender=Order)
def post_save_order(instance, *args, **kwargs):
    """
    This signal will save order with order id in ORD000001,... format.
    """
    order_id = "{}{:06d}".format('ORD', instance.id)
    instance.order = order_id
