# Generated by Django 4.0.4 on 2023-08-29 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image1',
            field=models.BinaryField(blank=True, editable=True, null=True, verbose_name='Product Image 1'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=models.BinaryField(blank=True, editable=True, null=True, verbose_name='Product Image 2'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image3',
            field=models.BinaryField(blank=True, editable=True, null=True, verbose_name='Product Image 3'),
        ),
    ]
