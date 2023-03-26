# Generated by Django 4.1.3 on 2023-03-25 12:50

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0024_products_new_arrival"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="category",
            field=products.models.ModifiedArrayField(
                base_field=models.CharField(
                    blank=True,
                    choices=[
                        ("Deal of the day", "Deal of the day"),
                        ("best-seller", "Best Seller"),
                        ("Trend Products", "Trend Products"),
                        ("Featured Products", "Featured Products"),
                        ("Biscuits & Snacks", "Biscuits & Snacks"),
                        ("Bread & Bakery", "Bread & Bakery"),
                        ("Breakfast & Dairy", "Breakfast & Dairy"),
                        ("Frozen Foods", "Frozen Foods"),
                        ("Fruits & Vegetables", "Fruits & Vegetables"),
                        ("Grocery & Staples", "Grocery & Staples"),
                        ("Household Needs", "Household Needs"),
                        ("Meats & Seafood", "Meats & Seafood"),
                        ("Eggs Substitutes", "Eggs Substitutes"),
                        ("Honey Vegetables", "Honey Vegetables"),
                        ("Marmalades Staples", "Marmalades Staples"),
                        ("Sour Cream and Dips", "Sour Cream and Dips"),
                        ("Yogurt Seafood", "Yogurt Seafood"),
                    ],
                    max_length=255,
                    null=True,
                    verbose_name="Product Category",
                ),
                null=True,
                size=None,
            ),
        ),
    ]
