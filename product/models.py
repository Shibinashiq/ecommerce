from django.db import models


# Create your models here.
class Product(models.Model):
    product_image = models.ImageField(upload_to='product_image/' , null=True)
    product_name = models.CharField(max_length=255 , null=True)  # Changed to CharField for product name
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Changed to DecimalField for product price
    product_brand = models.CharField(max_length=255, null=True)  # Changed to CharField for product brand
    product_offer = models.CharField(max_length=25, null=True)
    product_category = models.CharField(max_length=50, null=True)
    product_quantity = models.PositiveIntegerField(null=True)  # Changed to PositiveIntegerField for quantity
   

    # def __str__(self):
    #     return self.product_name  # Updated to use the correct field name for string representation
