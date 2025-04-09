from rest_framework import generics
from .models import Cart, Product, Category, Transaction, DetailTransaction
from .serializers import (CartSerializers, ProductSerializers,
                          CategorySerializers, TransactionySerializers,
                          DetailTransactionSerializers)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
