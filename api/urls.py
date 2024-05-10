from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, SubcategoryViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('subcategories', SubcategoryViewSet, basename='subcategories')
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
]

