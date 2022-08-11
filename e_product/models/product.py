from django.db import models

from e_category.models.category import Category
from ecommerce.managers.base_manager import BaseManager
from ecommerce.models.base_model import BaseModel


class Product(BaseModel):

    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=False)
    price = models.BigIntegerField(null=False, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = BaseManager()

    class Meta(BaseModel.Meta):
        db_table = 'e_products'
