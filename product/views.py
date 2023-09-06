from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet
from ecommerce.pagination import CustomLimitOffsetPagination
from product.models import Product
from product.serializers import ProductSerializer


class ProductView(ModelViewSet):
    """
    ModelViewSet for product model provides the following actions.

    create: Create a new product instance.
    retrieve: Return the given product.
    update: Update the given product instance.
    partial_update: Partially update the given product instance.
    destroy: Deletes the given product instance.
    list: Return a list of all existing products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    pagination_class = CustomLimitOffsetPagination
    filterset_fields = ['name', 'category']

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super(ProductView, self).get_serializer(*args, **kwargs)
