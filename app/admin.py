from django.contrib import admin
from .models import Product, Favorite
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'descripcion','categoria', 'price',)
	list_filter = ('name', 'categoria',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
	list_display = ('user', 'product', )
