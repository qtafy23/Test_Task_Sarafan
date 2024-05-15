from django.shortcuts import get_object_or_404
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

    id_category = serializers.IntegerField(source='category.id')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Subcategory
        fields = (
            'id',
            'name',
            'id_category',
            'category',
            'slug',
            'image',
        )


class ShortSubcategorySerializer(serializers.ModelSerializer):
    """Serializer for representation subcategory in product."""

    category = serializers.CharField(source='category.name')

    class Meta:
        model = Subcategory
        fields = (
            'id',
            'name',
            'category',
        )


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for product."""

    subcategory = ShortSubcategorySerializer()

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


class ProductListSerializer(serializers.ModelSerializer):
    """Serializer of product for shopping list."""

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'price',
        )


class ShoppingListSerializer(serializers.ModelSerializer):
    """Serializer for shopping list."""

    user = serializers.ReadOnlyField()
    product = serializers.ReadOnlyField()

    class Meta:
        model = ShoppingList
        fields = (
            'user',
            'product',
            'amount',
        )

    def validate(self, data):
        try:
            data['amount']
        except KeyError:
            raise serializers.ValidationError(
                {
                    'amount': 'required integer field'
                }
            )
        product_id = self.context['product_id']
        user = self.context['request'].user
        if ShoppingList.objects.filter(
            user=user, product=product_id
        ).exists():
            raise serializers.ValidationError(
                'This product has already been included in the shopping list!'
            )
        return data

    def create(self, validated_data):
        product = get_object_or_404(Product, pk=validated_data['id'])
        ShoppingList.objects.create(
            user=self.context['request'].user,
            product=product,
            amount=validated_data['amount'],
        )
        serializer = ProductListSerializer(product)
        return serializer.data


class ShoppingListGetSerializer(serializers.ModelSerializer):
    """Serializer for representing products."""

    product = serializers.CharField(source='product.name')
    price = serializers.IntegerField(source='product.price')

    class Meta:
        model = ShoppingList
        fields = (
            'product',
            'price',
            'amount',
        )
