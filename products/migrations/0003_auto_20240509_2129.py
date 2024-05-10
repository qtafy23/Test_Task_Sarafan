# Generated by Django 3.2.16 on 2024-05-09 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_shoppinglist_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, help_text='Attach an image', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='large_image',
            field=models.ImageField(blank=True, help_text='Attach an image large size.', null=True, upload_to='media/Limages/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='medium_image',
            field=models.ImageField(blank=True, help_text='Attach an image medium size.', null=True, upload_to='media/Mimages/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='small_image',
            field=models.ImageField(blank=True, help_text='Attach an image small size.', null=True, upload_to='media/Simages/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subcategory', to='products.category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, help_text='Attach an image', null=True, upload_to='media/'),
        ),
    ]