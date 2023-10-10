from django.db import models

# Create your models here.


class Category(models.Model):
    cat_image = models.ImageField(upload_to='cat_photos')
    category_name = models.CharField(max_length=25)
    brand = models.CharField(max_length=50)  # Add a field for brand
    description = models.TextField()  # Add a field for description
    

    def __str__(self):
        return self.category_name  # Define a string representation for the model









