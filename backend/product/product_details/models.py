from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="product/")

    def __str__(self):
        return self.title