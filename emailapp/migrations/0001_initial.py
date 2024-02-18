# Generated by Django 4.1.3 on 2024-02-18 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DelayDeliveryAndRefundEmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Delivery Delay', 'Delivery Delay'), ('Refund Requested', 'Refund Requested'), ('Refund Processed', 'Refund Processed'), ('Refunded', 'Refunded')], default='', max_length=200, null=True)),
                ('email_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('body', models.TextField(blank=True, default='', null=True)),
                ('sms_body', models.TextField(blank=True, default='', null=True)),
                ('sender', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('templateid', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('DltPrincipalEntityId', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 18, 19, 2, 22, 812548), null=True)),
            ],
            options={
                'verbose_name': 'DelayDeliveryAndRefundEmail',
                'verbose_name_plural': 'DelayDeliveryAndRefundEmails',
            },
        ),
        migrations.CreateModel(
            name='PaymentsEmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Retry', 'Retry'), ('Failed', 'Failed'), ('Successfull', 'Successfull'), ('Complaint', 'Complaint')], default='', max_length=200, null=True)),
                ('email_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('body', models.TextField(blank=True, default='', null=True)),
                ('sms_body', models.TextField(blank=True, default='', null=True)),
                ('sender', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('templateid', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 18, 19, 2, 22, 812099), null=True)),
            ],
            options={
                'verbose_name': 'PaymentsEmail',
                'verbose_name_plural': 'PaymentsEmails',
            },
        ),
        migrations.CreateModel(
            name='PromotionalEmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Reccuring', 'Reccuring'), ('Promotional Offer', 'Promotional Offer')], default='', max_length=200, null=True)),
                ('email_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('body', models.TextField(blank=True, default='', null=True)),
                ('sms_body', models.TextField(blank=True, default='', null=True)),
                ('sender', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('templateid', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('DltPrincipalEntityId', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 18, 19, 2, 22, 812419), null=True)),
            ],
            options={
                'verbose_name': 'PromotionalEmail',
                'verbose_name_plural': 'PromotionalEmails',
            },
        ),
        migrations.CreateModel(
            name='UserRegisteredEmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('New Registration', 'New Registration'), ('New Registration to admin', 'New Registration to admin')], default='', max_length=200, null=True)),
                ('email_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('body', models.TextField(blank=True, default='', null=True)),
                ('sms_body', models.TextField(blank=True, default='', null=True)),
                ('sender', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('templateid', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('DltPrincipalEntityId', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 18, 19, 2, 22, 812236), null=True)),
            ],
            options={
                'verbose_name': 'UserRegisteredEmail',
                'verbose_name_plural': 'UserRegisteredEmails',
            },
        ),
    ]