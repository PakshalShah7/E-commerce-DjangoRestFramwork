""" This file contains product serializer which is used in project. """

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from product.models import Product


class ProductListSerializer(serializers.ListSerializer):
    """
    This is list serializer for product serializer.
    """
    def create(self, validated_data):
        """
        This method just creates the actual model instance using the validated_data.
        """
        products = [Product(**category) for category in validated_data]
        return Product.objects.bulk_create(products)

    def update(self, instance, validated_data):
        """
        This method just updates the actual model instance using the validated_data.
        """
        return_list = []
        for data in validated_data:
            if "id" in data and data['id'] not in ['', None]:
                Product.objects.filter(id=data['id']).update(**data)
                return_list.append(data)
            else:
                return_list.append(Product.objects.create(**data))
        return return_list


class ProductSerializer(ModelSerializer):
    """
    This is model serializer for product model.
    """
    id = serializers.IntegerField(required=False)

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options,verbose_name, and a lot of other options.
        """
        model = Product
        list_serializer_class = ProductListSerializer
        fields = ['id', 'created', 'modified', 'name', 'description', 'price', 'image', 'stock',
                  'category']
