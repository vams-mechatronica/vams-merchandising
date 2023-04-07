# Generated by Django 4.1.3 on 2023-04-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_rename_image_products_image1_products_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='product/media/mainImage/%Y/%m/%d', verbose_name='Product Image 1'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='product/media/secondaryImage/%Y/%m/%d', verbose_name='Product Image 2'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image3',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='product/media/tertiaryImage/%Y/%m/%d', verbose_name='Product Image 3'),
        ),
    ]
