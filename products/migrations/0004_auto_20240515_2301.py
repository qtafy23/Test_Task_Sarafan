# Generated by Django 3.2.16 on 2024-05-15 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240509_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',), 'verbose_name': 'category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('id',), 'verbose_name': 'subcategory', 'verbose_name_plural': 'Subcategories'},
        ),
    ]