# Generated by Django 4.2.1 on 2024-03-01 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='product.lesson'),
        ),
    ]