from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from e_product.views.product import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]