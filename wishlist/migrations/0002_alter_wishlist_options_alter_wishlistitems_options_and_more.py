# Generated by Django 4.1.3 on 2023-04-11 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name_plural': 'Wishlist'},
        ),
        migrations.AlterModelOptions(
            name='wishlistitems',
            options={'verbose_name_plural': 'WishlistItems'},
        ),
        migrations.RemoveField(
            model_name='wishlistitems',
            name='ordered',
        ),
    ]