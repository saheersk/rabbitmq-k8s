from django.urls import path

from api.v1.order.views import OrderView


urlpatterns = [
    path("<int:id>/", OrderView.as_view(), name="order"),
]