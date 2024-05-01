from django.contrib import admin

# Register your models here.
# market/admin.py
from django.contrib import admin
from market.models import CustomUser, Product, Order

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_seller', 'is_buyer', 'company_name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'seller', 'price', 'quantity']
    search_fields = ['name', 'seller__username', 'seller__company_name']
    list_filter = ['seller', 'price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer', 'product', 'quantity', 'created_at']
    list_filter = ['buyer', 'created_at']
    search_fields = ['buyer__username', 'product__name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)