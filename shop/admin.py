from django.contrib import admin
from .models import Category, Brand, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class CategoryBrand(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Brand, CategoryBrand)


class CategoryProduct(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'old_price',
                    'rate', 'stock', 'avaliable', 'created', 'updated']
    list_filter = ['avaliable', 'created', 'updated', 'rate']
    list_editable = ['price', 'old_price', 'stock', 'avaliable']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, CategoryProduct)
