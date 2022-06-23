from django.contrib import admin
from .models.products import Product
from .models.categorys import Category
from .models.customers import Customer

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'categorys']

class AdminCategory(admin.ModelAdmin):
    list_display= ['name']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)