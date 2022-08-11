from django.http import Http404
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from e_order.services.order import OrderService
from e_product.models import Product
from e_product.serializers.product import ProductSerializer
from ecommerce.throttles.product import ProductRateThrottle


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]
    throttle_classes = [ProductRateThrottle]

    def get_object(self):
        product = Product.objects.filter(pk=self.kwargs.get('pk')).first()
        if not product:
            raise Http404
        return product

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()

        if OrderService.exists_by_product_id(product.id):
            raise ValidationError({'product': "This product already used."})

        product.deleted = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # @action(detail=False, methods=['POST'], url_path='bulk_create')
    # def bulk_create(self, request):
    #     print(request.data)
    #     return Response(status=status.HTTP_201_CREATED)
