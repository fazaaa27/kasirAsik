from rest_framework import serializers
from .models import Cart, Product, Category, Transaction, DetailTransaction


class ProductSerializers(serializers.ModelSerializers):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock", "category"]