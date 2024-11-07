from django.urls import include, path
from rest_framework import routers

from order.viewsets import order_viewset

router = routers.SimpleRouter()
router.register(r"order", order_viewset.OrderViewSet, basename="order")


urlpatterns = [
    path("", include(router.urls)),
]