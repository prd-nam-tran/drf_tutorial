from e_category.models import Category


class CategoryService:

    @classmethod
    def exists_category_name(cls, instance, data):
        queryset = Category.objects.filter(name=data.get('name'))

        if instance:
            queryset = queryset.exclude(pk=instance.pk)

        return queryset.exists()

    @classmethod
    def exists_by_id(cls, pk):
        return Category.objects.filter(pk=pk).exists()
