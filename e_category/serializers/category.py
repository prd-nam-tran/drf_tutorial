from rest_framework import serializers

from e_category.models import Category
from e_category.services.category import CategoryService


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['deleted']

    def validate(self, data):
        if CategoryService.exists_category_name(self.instance, data):
            raise serializers.ValidationError({'name': "This category name already exist."})

        return data


class CategoryInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
