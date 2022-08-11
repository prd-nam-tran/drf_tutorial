from rest_framework.throttling import UserRateThrottle


class ProductRateThrottle(UserRateThrottle):
    scope = 'product_rate'
