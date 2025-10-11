from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    name = models.CharField(max_length=50)  # Combo Offer, Veg, Non-Veg

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/")  # media/products/
    price = models.DecimalField(max_digits=6, decimal_places=2)
    review = models.FloatField(default=0)

    def __str__(self):
        return self.name


# order model
class Order(models.Model):
    STATUS_CHOICES = [
        ('Processing', 'Processing'),
        ('Ready', 'Ready'),
        ('Delivered', 'Delivered'),
    ]

    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Processing')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
