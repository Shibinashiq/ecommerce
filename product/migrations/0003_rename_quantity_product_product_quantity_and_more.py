# Generated by Django 4.2.4 on 2023-10-11 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_offer_id_alter_product_product_brand_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='product_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='offer_id',
        ),
    ]