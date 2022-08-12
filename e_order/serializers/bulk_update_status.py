from rest_framework import serializers

from e_order.services.order import OrderService


class BulkUpdateStatusSerializer(serializers.Serializer):

    status = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    ids = serializers.ListField(allow_empty=False)

    class Meta:
        fields = ['ids', 'status']

    def validate(self, data):
        order_ids = data.get('ids')

        if OrderService.count_by_ids_and_not_status(order_ids, "PAID") != len(order_ids):
            raise serializers.ValidationError({'order_ids': 'Invalid ids.'})

        return data
