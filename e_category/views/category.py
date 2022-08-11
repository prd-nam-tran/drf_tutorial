from django.http import Http404
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from e_category.models import Category
from e_category.serializers.category import CategorySerializer
from e_product.services.Product import ProductService
from ecommerce.throttles.category import CategoryRateThrottle


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    throttle_classes = [CategoryRateThrottle]

    def get_object(self):
        category = Category.objects.filter(pk=self.kwargs.get('pk')).first()
        if not category:
            raise Http404
        return category

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()

        if ProductService.exists_by_category_id(category.id):
            raise ValidationError({'category': "This category already used."})

        category.deleted = True
        category.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
