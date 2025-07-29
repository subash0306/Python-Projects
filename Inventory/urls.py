from django.urls import path
from .views import *

urlpatterns = [
    path('products/add/', ProductsAdd),
    path('products/', ShowProducts),
    path('products/delect/<int:id>/', DeleteProducts, name='product_delete'),
    path('products/update/<int:id>/', UpdateProduct, name='product_update'),
]
