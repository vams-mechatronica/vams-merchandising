# Generated by Django 4.0.4 on 2023-09-14 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user/20230914', verbose_name='Avatar'),
        ),
    ]