from django.db import models

from e_product.models import Product
from ecommerce.managers.base_manager import BaseManager
from ecommerce.models.base_model import BaseModel


class Order(BaseModel):

    order_date = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    quantity = models.IntegerField(null=False, default=0)
    total_price = models.BigIntegerField(null=False, default=0)
    status = models.CharField(max_length=50, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    objects = BaseManager()

    class Meta(BaseModel.Meta):
        db_table = 'e_orders'
