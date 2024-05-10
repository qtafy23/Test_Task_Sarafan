from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import (CategorySerializer, SubcategorySerializer,
                          ProductSerializer,)
from products.models import Category, Subcategory, Product


class CategoryViewSet(ReadOnlyModelViewSet):
    """Viewset for category."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(ReadOnlyModelViewSet):
    """Viewset for subcategory."""

    queryset = Subcategory.objects.all().select_related('category')
    serializer_class = SubcategorySerializer


class ProductViewSet(ReadOnlyModelViewSet):
    """Viewset for product."""

    queryset = Product.objects.all().select_related('subcategory')
    serializer_class = ProductSerializer
