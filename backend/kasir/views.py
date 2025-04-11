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

class ProductRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_url_kwarg = "product_id"
    permission_classes = [IsAuthenticated]
