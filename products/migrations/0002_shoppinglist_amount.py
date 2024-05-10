# Generated by Django 3.2.16 on 2024-05-09 20:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='amount',
            field=models.PositiveIntegerField(blank=True, default=1, validators=[django.core.validators.MaxValueValidator(10000, message='Amount must be less then 10000!')]),
            preserve_default=False,
        ),
    ]
