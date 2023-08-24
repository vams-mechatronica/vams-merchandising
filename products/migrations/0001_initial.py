# Generated by Django 4.0.4 on 2023-08-17 05:07

from django.db import migrations, models
import django_quill.fields
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', products.models.ModifiedArrayField(base_field=models.CharField(blank=True, choices=[('homepage', 'HOME PAGE'), ('categoriespage', 'CATEGORIES PAGE'), ('productpage', 'PRODUCT PAGE'), ('top', 'TOP'), ('middle', 'MIDDLE'), ('bottom', 'BOTTOM'), ('right', 'RIGHT'), ('left', 'LEFT'), ('newarrival', 'NEW ARRIVAL'), ('men', 'MEN'), ('kids', 'KIDS'), ('women', 'WOMEN'), ('cosmetics', 'COSMETICS'), ('browse-more', 'Browse More')], max_length=255, null=True, verbose_name='Banner Position'), blank=True, null=True, size=None)),
                ('banner_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Banner Name')),
                ('banner_desc', django_quill.fields.QuillField(blank=True, null=True)),
                ('banner_images', models.ImageField(upload_to='banners/media/images/%Y/%m/%d', verbose_name='Banner Image')),
                ('banner_status', models.CharField(choices=[('Activate', 'ACTIVATE'), ('Deactivate', 'DEACTIVATE')], default=None, max_length=20)),
                ('products_available', models.IntegerField(blank=True, null=True, verbose_name='Products Available')),
            ],
            options={
                'verbose_name_plural': 'Banners',
                'db_table': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(default=None, max_length=255, unique=True)),
                ('desc', models.TextField(blank=True, default=None, max_length=1024, null=True)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='category/media/photos/%Y/%m/%d', verbose_name='category image')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoriesProducts',
            fields=[
                ('categoriesproduct_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'CategoriesProducts',
                'db_table': 'CategoriesProducts',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='product/media/photos/%Y/%m/%d', verbose_name='Product_Image')),
                ('image_thumbnail', models.ImageField(blank=True, null=True, upload_to='product/media/photos/%Y/%m/%d/thumbnails', verbose_name='Product Image Thumbnail')),
                ('image_thumbnail_color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Product Thumbnail Color')),
            ],
            options={
                'verbose_name_plural': 'ProductImages',
                'db_table': 'ProductImages',
            },
        ),
        migrations.CreateModel(
            name='ProductReviewAndRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Product Review')),
                ('ratings', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Product Rating')),
                ('review_date', models.DateTimeField(auto_now=True, verbose_name='review_date')),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'ProductReviewAndRatings',
                'db_table': 'ProductReviewAndRatings',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('longname', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('desc', django_quill.fields.QuillField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=50)),
                ('category', products.models.ModifiedArrayField(base_field=models.CharField(blank=True, choices=[('new-arrival', 'New Arrival'), ('best-seller', 'Best Seller'), ('trending', 'Trend Products'), ('Featured Products', 'Featured Products'), ('kids-collection', 'Kids Collection'), ('hot-collection', 'Hot Collection')], max_length=255, null=True, verbose_name='Product Category'), null=True, size=None)),
                ('max_retail_price', models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='MRP (in Rs.)')),
                ('image1', models.ImageField(blank=True, default=None, null=True, upload_to='product/media/mainImage/%Y/%m/%d', verbose_name='Product Image 1')),
                ('image2', models.ImageField(blank=True, default=None, null=True, upload_to='product/media/secondaryImage/%Y/%m/%d', verbose_name='Product Image 2')),
                ('image3', models.ImageField(blank=True, default=None, null=True, upload_to='product/media/tertiaryImage/%Y/%m/%d', verbose_name='Product Image 3')),
                ('brand', models.CharField(blank=True, max_length=50, null=True, verbose_name='Brand')),
                ('available_sizes', products.models.ModifiedArrayField(base_field=models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXL', 'XXL')], max_length=255, null=True, verbose_name='Product Available'), null=True, size=None)),
                ('vendor', models.CharField(blank=True, max_length=50, null=True, verbose_name='Vendor')),
                ('tags', products.models.ModifiedArrayField(base_field=models.CharField(blank=True, choices=[('cotton', 'Cotton'), ('synthetic', 'Synthetic'), ('woolen', 'Woolen'), ('polyster', 'Polyster')], max_length=50, null=True, verbose_name='Tags'), null=True, size=None)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Discount (in %)')),
                ('stock', models.IntegerField(default=0, verbose_name='available stock (in Nos.)')),
                ('display_home', models.BooleanField(default=False, verbose_name='Display at home')),
                ('new_arrival', models.BooleanField(default=False, verbose_name='New')),
                ('average_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('status', models.BooleanField(default=True, verbose_name='Product Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'db_table': 'Products',
            },
        ),
    ]
