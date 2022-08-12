from rest_framework import serializers

from e_product.serializers.product import ProductSerializer


class BulkCreateProductSerializer(serializers.Serializer):

    products = ProductSerializer(many=True, allow_null=False)

    class Meta:
        fields = ['products']
