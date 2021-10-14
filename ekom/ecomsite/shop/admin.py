from django.contrib import admin
from .models import Products
# Register your models here.


admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC SHOPPING"
admin.site.index_title = "Manage ABC SHOPPING"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price','discount_price','category','image')
    search_fields=('title')
admin.site.register(Products)