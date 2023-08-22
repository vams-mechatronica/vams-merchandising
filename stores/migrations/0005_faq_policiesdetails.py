# Generated by Django 3.2.5 on 2023-08-18 15:31

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_remove_storeproductsdetails_discount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=500, verbose_name='FAQ Question')),
                ('answer', models.TextField(max_length=5000, verbose_name='FAQ Answer')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
        migrations.CreateModel(
            name='PoliciesDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refund_policy', django_quill.fields.QuillField()),
                ('return_policy', django_quill.fields.QuillField()),
                ('shipping_and_delivery_policy', django_quill.fields.QuillField()),
                ('payment_type', django_quill.fields.QuillField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.storedetail', verbose_name='Store')),
            ],
            options={
                'verbose_name': 'PoliciesDetails',
                'verbose_name_plural': 'PoliciesDetailss',
            },
        ),
    ]