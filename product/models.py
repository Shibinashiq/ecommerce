from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)  # Changed to CharField for product name
    product_price = models.DecimalField(max_digits=10, decimal_places=2)  # Changed to DecimalField for product price
    product_brand = models.CharField(max_length=255)  # Changed to CharField for product brand
    product_offer = models.CharField(max_length=25)
    product_category = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()  # Changed to PositiveIntegerField for quantity
    offer_id = models.CharField(max_length=255)  # Changed to CharField for offer ID

    def __str__(self):
        return self.product_name  # Updated to use the correct field name for string representation
