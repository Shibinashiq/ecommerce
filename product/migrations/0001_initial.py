# Generated by Django 4.2.4 on 2023-10-10 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_brand', models.CharField(max_length=255)),
                ('product_offer', models.CharField(max_length=25)),
                ('product_category', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('offer_id', models.CharField(max_length=255)),
            ],
        ),
    ]