from e_order.models import Order


class OrderService:

    @classmethod
    def calculate_total_price(cls, order):
        return order.get('quantity') * order.get('product').price

    @classmethod
    def exists_by_product_id(cls, product_id):
        return Order.objects.filter(product__id=product_id).exists()
