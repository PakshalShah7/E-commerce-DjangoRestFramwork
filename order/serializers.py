""" This file contains order and transaction detail serializers which are used in project. """

from http import HTTPStatus
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from cart.models import Cart
from order.models import Order, OrderInvoice


class OrderSerializer(ModelSerializer):
    """
    This is model serializer for order model.
    """

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Order
        fields = ['order', 'total_amount', 'status', 'delivery_address']

    def create(self, validated_data):
        """
        This method just creates the actual model instance using the validated data.
        """
        cart = Cart.objects.get(user=self.context['request'].user, status=True)
        if cart.set_total > 0:
            order = Order.objects.create(cart=cart, user=self.context['request'].user,
                                         delivery_address=validated_data['delivery_address'],
                                         total_amount=cart.set_total)
            cart.status = False
            cart.save()
            order.save()
            order_invoice = OrderInvoice.objects.create(user=self.context['request'].user,
                                                        amount=order.total_amount, order=order,
                                                        delivery_address=order.delivery_address)
            order_invoice.save()
        else:
            return Response(data="You have no items in cart", status=HTTPStatus.NO_CONTENT)
        return order


class OrderInvoiceSerializer(ModelSerializer):
    """
    This is model serializer for order invoice model.
    """

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = OrderInvoice
        fields = '__all__'
