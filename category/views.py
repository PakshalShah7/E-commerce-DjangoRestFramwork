from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from category.models import Category
from category.serializers import CategorySerializer
from ecommerce.pagination import CustomLimitOffsetPagination


class CategoryView(ModelViewSet):
    """
    ModelViewSet for category model provides the following actions.

    create: Create a new category instance.
    retrieve: Return the given category.
    update: Update the given category instance.
    partial_update: Partially update the given category instance.
    destroy: Deletes the given category instance.
    list: Return a list of all existing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomLimitOffsetPagination
    filterset_fields = ['name']
