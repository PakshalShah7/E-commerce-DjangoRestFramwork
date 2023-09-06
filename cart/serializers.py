""" This file contains cart and cart item serializers which are used in project. """

from rest_framework.serializers import ModelSerializer
from cart.models import Cart, CartItem


class CartItemSerializer(ModelSerializer):
    """
    This is model serializer for cart item model.
    """

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = CartItem
        fields = ['id', 'item', 'quantity', 'sub_total']

    def create(self, validated_data):
        """
        This method just creates the actual model instance using the validated_data.
        """
        cart, cart_created = Cart.objects.get_or_create(user=self.context['request'].user, status=True)
        cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, item=validated_data['item'])
        if cart_item_created:
            cart_item.quantity = int(validated_data['quantity'])
            cart_item.save()
        else:
            cart_item.quantity = cart_item.quantity + int(validated_data['quantity'])
            cart_item.save()
        return cart_item

    def to_representation(self, instance):
        """
        This method will represent item as name instead of its id.
        """
        rep = super(CartItemSerializer, self).to_representation(instance)
        rep['item'] = instance.item.name
        return rep


class CartSerializer(ModelSerializer):
    """
    This is model serializer for cart model.
    """
    carts = CartItemSerializer(many=True)

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Cart
        fields = ['user', 'status', 'set_total', 'carts']
