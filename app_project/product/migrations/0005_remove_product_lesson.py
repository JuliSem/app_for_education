# Generated by Django 4.2.1 on 2024-03-01 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_date_created_product_date_create'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='lesson',
        ),
    ]
