from django.db.models import Q
from django.http import Http404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from e_order.models import Order
from e_order.serializers.bulk_update_status import BulkUpdateStatusSerializer
from e_order.serializers.order import OrderSerializer
from e_order.services.order import OrderService
from ecommerce.throttles.order import OrderRateThrottle


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]
    throttle_classes = [OrderRateThrottle]

    def get_queryset(self):
        queryset = Order.objects.all()
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(Q(product__name__icontains=name)
                                       | Q(product__category__name__icontains=name))
        return queryset

    def get_object(self):
        order = Order.objects.filter(pk=self.kwargs.get('pk')).first()
        if not order:
            raise Http404
        return order

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            serializer.save(total_price=OrderService.calculate_total_price(data),
                            created_by=self.request.user,
                            updated_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(dict(errors=serializer.errors), status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrderSerializer(instance, data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            serializer.save(total_price=OrderService.calculate_total_price(data),
                            updated_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(dict(errors=serializer.errors), status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        order.deleted = True
        order.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['PUT'], url_path='bulk_update_status',
            serializer_class=BulkUpdateStatusSerializer)
    def bulk_update_status(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            Order.objects.filter(pk__in=data.get('ids')).update(status=data.get('status'))
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(dict(errors=serializer.errors), status.HTTP_400_BAD_REQUEST)
