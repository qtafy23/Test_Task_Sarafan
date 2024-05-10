from rest_framework import serializers

from products.models import Category, Subcategory, Product, ShoppingList


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category."""

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'image',
        )


class SubcategorySerializer(serializers.ModelSerializer):
    """Serializer for subcategory."""

    category = CategorySerializer()

    class Meta:
        model = Subcategory
        fields = (
            'id',
            'name',
            'category',
            'slug',
            'image',
        )


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for product."""

    subcategory = SubcategorySerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'subcategory',
            'slug',
            'small_image',
            'medium_image',
            'large_image',
        )
