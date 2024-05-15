from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, SubcategoryViewSet,
                    ProductViewSet, ShoppingListViewSet)

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('subcategories', SubcategoryViewSet, basename='subcategories')
router.register('products', ProductViewSet, basename='products')
router.register('shoppinglist', ShoppingListViewSet, basename='shoppinglist')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
