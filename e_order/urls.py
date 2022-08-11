from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from e_order.views.order import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
