from django.contrib import admin

from .models import Category, Subcategory, Product, ShoppingList


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name', 'slug')
    save_on_top = True


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name', 'slug')
    save_on_top = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name', 'slug')
    save_on_top = True


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_display_links = ('user', 'product',)
    search_fields = ('user__username', 'product__name')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            'product', 'user',
        )
