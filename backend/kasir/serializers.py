from rest_framework import serializers
from .models import Cart, Product, Category, Transaction, DetailTransaction


class ProductSerializers(serializers.ModelSerializers):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock", "category"]


class CartSerializers(serializers.ModelSerializers):
    class Meta:
        model = Cart
        fields = ["id", "amount", "product"]


class CategorySerializers(serializers.ModelSerializers):
    class Meta:
        model = Category
        fields = ["id", "name"]


class TransactionySerializers(serializers.ModelSerializers):
    class Meta:
        model = Transaction
        fields = ["id", "date", "amount"]


class DetailTransactionSerializers(serializers.ModelSerializers):
    class Meta:
        model = DetailTransaction
        fields = ["id", "transactrion", "product", "amount"]