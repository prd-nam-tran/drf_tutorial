from rest_framework.throttling import UserRateThrottle


class CategoryRateThrottle(UserRateThrottle):
    scope = 'category_rate'
