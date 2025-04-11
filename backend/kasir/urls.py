from django.urls import path
from . import views


urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="product-list"),
    path("products/<int:product_id>", views.ProductRetrieveView.as_view(), name="product-retrieve"),
    path("category/", views.CategoryListView.as_view(), name="category-list"),
    path("category/<int:category_id>", views.CategoryRetrieveView.as_view(), name="category-retrieve"),
    path("cart/", views.CartListView.as_view(), name="cart-list"),
    path("cart/<int:cart_id>", views.CartRetrieveView.as_view(), name="cart-retrieve"),
    path("transaction/", views.TransactionListView.as_view(), name="transaction-list"),
    path("transaction/<int:transaction_id>", views.TransactionRetrieveView.as_view(), name="transaction-retrieve"),
    path("detail_transaction/", views.DetailTransactionListView.as_view(), name="detail-transaction-list"),
    path("detail_transaction/<int:detail_transaction_id>", views.DetailTransactionRetrieveView.as_view(), name="detail-transaction-retrieve"),
]