# Generated by Django 4.2.1 on 2024-03-01 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_product_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='product.lesson'),
        ),
    ]