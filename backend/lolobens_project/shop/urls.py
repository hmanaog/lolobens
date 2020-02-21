from django.urls import path

from lolobens_project.shop.views.product import GetAllProduct, CreateNewProduct, RetrieveUpdateDestroyProduct

urlpatterns = [
    path('products/', GetAllProduct.as_view(), name='get all product'),
    path('products/new/', CreateNewProduct.as_view(), name='create new product'),
    path('products/<int:product_id>/', RetrieveUpdateDestroyProduct.as_view(), name='retrieve update destroy product'),
]