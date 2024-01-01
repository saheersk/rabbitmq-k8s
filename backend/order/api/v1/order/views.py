from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import OrderSerializer
from user_order.models import Order
from api.v1.order.utils import CustomTokenAuthentication


class OrderView(APIView):
    def get(self, request, id):
        orders = Order.objects.filter(user_id=id)
        serializer = OrderSerializer(orders, many=True)

        return Response({
            'orders': serializer.data
        }, status=status.HTTP_200_OK)