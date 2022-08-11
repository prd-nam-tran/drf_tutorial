from django.db import models

from ecommerce.managers.base_manager import BaseManager
from ecommerce.models.base_model import BaseModel


class Category(BaseModel):

    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=True)

    objects = BaseManager()

    class Meta(BaseModel.Meta):
        db_table = 'e_categories'
