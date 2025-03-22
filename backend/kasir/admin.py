from django.contrib import admin
from .models import Product, Cart, Category, Transaction, DetailTransaction


admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(DetailTransaction)