from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    """
    This model will store category details.
    """
    name = models.CharField(max_length=20)

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
        return self.name
