# Generated by Django 4.0.4 on 2023-08-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_remove_products_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreviewandratings',
            name='upload_image',
            field=models.ImageField(blank=True, null=True, upload_to='product/media/reviews/%Y/%m/%d', verbose_name='ImagesForReview'),
        ),
    ]
