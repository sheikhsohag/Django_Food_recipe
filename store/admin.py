from django.contrib import admin
from . models import Product, Review

# # Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('product_name',)}
    list_display = ['product_name', 'category','slug',]


admin.site.register(Product, ProductAdmin)


@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'date', 'rating']
