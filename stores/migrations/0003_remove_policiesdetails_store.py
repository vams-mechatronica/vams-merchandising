# Generated by Django 4.0.4 on 2023-09-03 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_alter_policiesdetails_payment_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policiesdetails',
            name='store',
        ),
    ]
