""" from django.contrib import admin
from .models import Supplier, Category, Product


admin.site.register(Supplier),
admin.site.register(Category),
admin.site.register(Product) """

from django.contrib import admin
from .models import Product, Category, Supplier


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    fields = ('name', 'price', 'quantity')



@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone')

    search_fields = ('name', 'contact_person')
    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    search_fields = ('name',)
    
    ordering = ('name',)
    
    inlines = [ProductInline]
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'supplier', 'stock_status')
    
    list_display_links = ('name',)
    
    list_editable = ('price', 'quantity')
    
    search_fields = ('name', 'category__name', 'supplier__name')
    
    
    def stock_status(self, obj):
        if obj.quantity == 0:
            return '❌ Sin Stock'
        elif obj.quantity < 10:
            return '⚠️ Stock Bajo'
        else:
            return '✅ Disponible'
    stock_status.short_description = 'Estado'
    

# Register your models here.
