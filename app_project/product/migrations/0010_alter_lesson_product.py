# Generated by Django 4.2.1 on 2024-03-01 12:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_product_lesson_product_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product', unique=True),
        ),
    ]
