from rest_framework import serializers

from e_category.services.category import CategoryService
from e_product.models import Product
from e_product.services.Product import ProductService


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['deleted']

    def validate(self, data):
        if ProductService.exists_product_name(self.instance, data):
            raise serializers.ValidationError({'name': "This product name already exist."})

        return data

    def to_internal_value(self, data):
        category_id = data.get('category', None)

        if not category_id:
            raise serializers.ValidationError({'category_id': "This field is required."})

        if category_id and not CategoryService.exists_by_id(category_id):
            raise serializers.ValidationError({'category': 'Object does not exist.'})

        return super().to_internal_value(data)
