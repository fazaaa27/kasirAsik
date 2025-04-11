from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Cart, Product, Category, Transaction, DetailTransaction
from .serializers import (CartSerializers, ProductSerializers,
                          CategorySerializers, TransactionySerializers,
                          DetailTransactionSerializers)

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsAuthenticated]
