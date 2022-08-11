from rest_framework import serializers

from e_order.models import Order
from e_product.services.Product import ProductService


class OrderSerializer(serializers.ModelSerializer):

    status = serializers.CharField(allow_null=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['deleted']

    def to_internal_value(self, data):
        product_id = data.get('product', None)

        if not product_id:
            raise serializers.ValidationError({'product_id': "This field is required."})

        if product_id and not ProductService.exists_by_id(product_id):
            raise serializers.ValidationError({'product': 'Object does not exist.'})

        return super().to_internal_value(data)
