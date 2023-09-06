from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from cart.models import Cart, CartItem
from cart.serializers import CartSerializer, CartItemSerializer
from ecommerce.pagination import CustomLimitOffsetPagination


class CartListView(ListAPIView):
    """
    This view will display cart that is specific to the user.
    """
    serializer_class = CartSerializer
    pagination_class = CustomLimitOffsetPagination

    def get_queryset(self):
        """
        Returns a cart that is specific to the user.
        """
        return Cart.objects.filter(user=self.request.user, status=True)


class CartItemView(ModelViewSet):
    """
    ModelViewSet for cart item model provides the following actions.

    create: Create a new cart item instance.
    retrieve: Return the given cart item.
    update: Update the given cart item instance.
    partial_update: Partially update the given cart item instance.
    destroy: Deletes the given cart item instance.
    list: Return a list of all existing cart items.
    """
    serializer_class = CartItemSerializer

    def get_queryset(self):
        """
        Returns a list of all cart items that is specific to the user.
        """
        return CartItem.objects.filter(cart__user=self.request.user)
