from django.db import models


class Order(models.Model):
    user_id = models.IntegerField()
    product_name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product_name