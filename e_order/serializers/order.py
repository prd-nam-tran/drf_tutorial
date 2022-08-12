from rest_framework import serializers

from e_order.models import Order
from e_product.services.Product import ProductService


class OrderSerializer(serializers.ModelSerializer):

    status = serializers.CharField(allow_null=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['deleted']

    def validate(self, data):
        product_id = data.get('product').id
        if product_id and not ProductService.exists_by_id(product_id):
            raise serializers.ValidationError({'product': 'Object does not exist.'})

        if ProductService.exists_product_name(self.instance, data):
            raise serializers.ValidationError({'name': "This product name already exist."})

        return data
