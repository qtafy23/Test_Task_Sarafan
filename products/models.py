from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    """Model for category."""

    name = models.CharField(
        max_length=124,
        unique=True,
    )
    slug = models.SlugField(
        max_length=124,
        unique=True,
    )
    image = models.ImageField(
        upload_to='media/',
        help_text='Attach an image',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """Model for subcategory."""

    name = models.CharField(
        max_length=124,
        unique=True,
    )
    slug = models.SlugField(
        max_length=124,
        unique=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='subcategory',
    )
    image = models.ImageField(
        upload_to='media/',
        help_text='Attach an image',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model for product."""

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.PROTECT,
        related_name='products',
    )
    name = models.CharField(
        max_length=124,
    )
    slug = models.SlugField(
        max_length=124,
        unique=True,
    )
    price = models.PositiveIntegerField()
    small_image = models.ImageField(
        upload_to='media/Simages/',
        help_text='Attach an image small size.',
        blank=True,
        null=True,
    )
    medium_image = models.ImageField(
        upload_to='media/Mimages/',
        help_text='Attach an image medium size.',
        blank=True,
        null=True,
    )
    large_image = models.ImageField(
        upload_to='media/Limages/',
        help_text='Attach an image large size.',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    """Model for interacting with a product in a shopping list."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shoppings',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='shoppings',
    )
    amount = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(
                10000,
                message='Amount must be less then 10000!'
            )
        ],
        blank=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'product'],
                name='uq_user_product'
            ),
        ]

    def __str__(self):
        return f'Products from shopping list {self.user}'
