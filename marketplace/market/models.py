from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    contact_info = models.EmailField(unique=True, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    # delivery_address = models.CharField(max_length=255, blank=True, null=True)

class Product(models.Model):
    seller = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    buyer = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.buyer.username}"