# Generated by Django 4.2.1 on 2024-03-01 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_lesson_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='lesson',
        ),
        migrations.AddField(
            model_name='product',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='product.lesson'),
        ),
    ]