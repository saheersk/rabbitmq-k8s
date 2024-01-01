from rest_framework import serializers

from product_details.models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image']

    def get_image(self, instance):
        request = self.context.get('request')
        if instance.image:
            return request.build_absolute_uri(instance.image.url)
        return None