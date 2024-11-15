from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),                   # List all products
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),  # View a product detail
    path('product/new/', views.ProductCreateView.as_view(), name='product_create'),       # Add a new product
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),  # Edit a product
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'), # Delete a product
]
