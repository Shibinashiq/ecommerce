# Generated by Django 4.2.4 on 2023-10-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_quantity_product_product_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=1, upload_to='product_image/'),
            preserve_default=False,
        ),
    ]
