""" This file contains category serializer which is used in project. """

from rest_framework.serializers import ModelSerializer
from category.models import Category


class CategorySerializer(ModelSerializer):
    """
    This is model serializer for category model.
    """

    class Meta:
        """
        Model Meta is basically the inner class of your model class.
        Model Meta is basically used to change the behavior of your model fields like changing
        order options, verbose_name, and a lot of other options.
        """
        model = Category
        fields = '__all__'
