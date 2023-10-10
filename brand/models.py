from django.db import models

class Brand(models.Model):
    Brand_image = models.ImageField(upload_to='brand_photos/')
    Brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Brand_name
