from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from e_category.views.category import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]


