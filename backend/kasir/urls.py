from django.urls import path
from . import views


urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="product-list"),
    path("products/<int:product_id>", views.ProductRetrieveView.as_view(), name="product-retrieve"),
]