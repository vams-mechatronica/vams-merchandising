# Generated by Django 5.0.3 on 2024-06-24 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VCReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=500)),
                ('avatar', models.BinaryField(blank=True, editable=True, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'VCReview',
                'verbose_name_plural': 'VCReviews',
            },
        ),
    ]
