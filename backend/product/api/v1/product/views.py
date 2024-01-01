from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer
from product_details.models import Product
from api.v1.product.producer import send_create_order


class ProductView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={ "request": request })

        return Response({
            'products': serializer.data
        }, status=status.HTTP_200_OK)
    

class OrderView(APIView):

    def get_product(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def post(self, request, id):
        product = self.get_product(id)

        if product is None:
            return HttpResponse("Product not found", status=status.HTTP_404_NOT_FOUND)

        if request.user.is_authenticated:
            order_details = {
                "user_id": request.user.id,
                "product_id": id,
                "product_name": product.title,
            }
        else:
            order_details = {
                "user_id": 3,
                "product_id": id,
                "product_name": product.title,
            }

        send_create_order(order_details)

        return HttpResponse("Order placed successfully!", status=status.HTTP_200_OK)
    