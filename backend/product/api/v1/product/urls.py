from django.urls import path

from api.v1.product.views import ProductView, OrderView


urlpatterns = [
    path("all/", ProductView.as_view(), name="product"),
    path("add/<int:id>/", OrderView.as_view(), name="order"),
]