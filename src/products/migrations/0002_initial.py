# Generated by Django 5.0.3 on 2024-06-24 04:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='productreviewandratings',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author Id'),
        ),
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand', verbose_name='Brand'),
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(blank=True, to='products.categories', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='products',
            name='seller',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Vendor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='products',
            name='subcategory',
            field=models.ManyToManyField(blank=True, to='products.categorysubcategories', verbose_name='Sub Category'),
        ),
        migrations.AddField(
            model_name='products',
            name='subsubcategory',
            field=models.ManyToManyField(blank=True, to='products.categorysubsubcategories', verbose_name='Sub Sub Category'),
        ),
        migrations.AddField(
            model_name='productreviewandratings',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='product rating'),
        ),
        migrations.AddField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='prodImages', to='products.products'),
        ),
        migrations.AddField(
            model_name='productsize',
            name='subcategory',
            field=models.ManyToManyField(blank=True, to='products.categorysubcategories', verbose_name='Sub Category'),
        ),
        migrations.AddField(
            model_name='products',
            name='available_sizes',
            field=models.ManyToManyField(to='products.productsize', verbose_name='Sizes'),
        ),
        migrations.AddField(
            model_name='producttag',
            name='category',
            field=models.ManyToManyField(to='products.categories', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='producttag',
            name='sub_category',
            field=models.ManyToManyField(to='products.categorysubcategories', verbose_name='_subcategory'),
        ),
        migrations.AddField(
            model_name='producttag',
            name='sub_sub_category',
            field=models.ManyToManyField(to='products.categorysubsubcategories', verbose_name='sub_sub_category'),
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='products.producttag', verbose_name='Tags'),
        ),
    ]
