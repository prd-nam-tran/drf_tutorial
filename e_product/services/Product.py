from e_product.models import Product


class ProductService:

    @classmethod
    def exists_product_name(cls, instance, data):
        queryset = Product.objects.filter(name=data.get('name'), category=data.get('category'))

        if instance:
            queryset = queryset.exclude(pk=instance.pk)

        return queryset.exists()

    @classmethod
    def exists_by_id(cls, pk):
        return Product.objects.filter(pk=pk).exists()

    @classmethod
    def exists_by_category_id(cls, category_id):
        return Product.objects.filter(category__id=category_id).exists()
