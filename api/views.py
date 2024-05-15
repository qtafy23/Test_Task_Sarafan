from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import (CategorySerializer, SubcategorySerializer,
                          ProductSerializer, ShoppingListSerializer, ShoppingListGetSerializer)
from products.models import Category, Subcategory, Product, ShoppingList


class CategoryViewSet(ReadOnlyModelViewSet):
    """View set for category."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(ReadOnlyModelViewSet):
    """View set for subcategory."""

    queryset = Subcategory.objects.all().select_related('category')
    serializer_class = SubcategorySerializer


class ProductViewSet(ReadOnlyModelViewSet):
    """View set for product."""

    queryset = Product.objects.all().select_related('subcategory')
    serializer_class = ProductSerializer

    @action(
            detail=True,
            methods=('post', 'delete', 'patch',),
            serializer_class=ShoppingListSerializer,
            permission_classes=(IsAuthenticated,),
    )
    def shopping_cart(self, request, pk=None):
        """Function for choosing a method for request."""

        if self.request.method == 'POST':
            return self.add_product_in_list(request, pk)
        elif self.request.method == 'DELETE':
            return self.remove_product_from_list(request, pk)
        elif self.request.method == 'PATCH':
            return self.patch_product_in_list(request, pk)

    def add_product_in_list(self, request, pk):
        """Function for adding a product to the shopping list."""

        serializer = self.get_serializer(
            data=request.data,
            context={'request': request, 'product_id': pk}
        )
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save(id=pk)
        return Response(
            response_data,
            status=status.HTTP_201_CREATED
        )

    @staticmethod
    def remove_product_from_list(request, pk):
        """Function for removing a product from the shopping list."""

        deleted_tuple = ShoppingList.objects.filter(
            user=request.user, product=pk
        ).delete()
        if deleted_tuple[0] == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch_product_in_list(self, request, pk):
        """Function for patching a product in the shopping list."""

        product = ShoppingList.objects.filter(
            user=request.user, product=pk
        ).delete()
        if product[0] == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request, 'product_id': pk}
        )
        serializer.is_valid(raise_exception=True)
        response_data = serializer.save(id=pk)
        return Response(
            response_data,
            status=status.HTTP_200_OK
        )

    @action(
        detail=False,
        methods=('post',),
    )
    def clear_shopping_list(self, request):
        """Function for cleaning the shopping list."""

        ShoppingList.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShoppingListViewSet(ReadOnlyModelViewSet):
    """View set for shopping list."""

    serializer_class = ShoppingListGetSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        return ShoppingList.objects.filter(
            user=self.request.user,
        ).select_related(
            'user',
            'product'
        )

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        total_products = len(data)
        total_sum = sum(
            item.get('price', 0) * item.get('amount', 0) for item in data
        )
        return Response(
            data={
                'total_products': total_products,
                'total_sum': total_sum,
                'products': data
            },
            status=status.HTTP_200_OK,
        )
