# Generated by Django 4.1.3 on 2023-04-07 18:31

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_products_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available_sizes',
            field=products.models.ModifiedArrayField(base_field=models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXL', 'XXL')], max_length=255, null=True, verbose_name='Product Available'), null=True, size=None),
        ),
    ]