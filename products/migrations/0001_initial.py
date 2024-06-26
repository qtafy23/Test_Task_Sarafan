# Generated by Django 3.2.16 on 2024-05-09 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124, unique=True)),
                ('slug', models.SlugField(max_length=124, unique=True)),
                ('image', models.ImageField(help_text='Attach an image', upload_to='media/')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('slug', models.SlugField(max_length=124, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('small_image', models.ImageField(help_text='Attach an image small size.', upload_to='media/Simages/')),
                ('medium_image', models.ImageField(help_text='Attach an image medium size.', upload_to='media/Mimages/')),
                ('large_image', models.ImageField(help_text='Attach an image large size.', upload_to='media/Limages/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124, unique=True)),
                ('slug', models.SlugField(max_length=124, unique=True)),
                ('image', models.ImageField(help_text='Attach an image', upload_to='media/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='products.category')),
            ],
            options={
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'Subcategories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoppings', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoppings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.subcategory'),
        ),
        migrations.AddConstraint(
            model_name='shoppinglist',
            constraint=models.UniqueConstraint(fields=('user', 'product'), name='uq_user_product'),
        ),
    ]
