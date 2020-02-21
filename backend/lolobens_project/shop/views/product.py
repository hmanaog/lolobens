from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from lolobens_project.shop.models.product import Product
from lolobens_project.shop.serializers.product import ProductSerializer
from lolobens_project.users.permissions import IsSuperUser


class GetAllProduct(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []


class CreateNewProduct(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSuperUser, IsAuthenticated]


class RetrieveUpdateDestroyProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSuperUser, IsAuthenticated]
    lookup_url_kwarg = 'product_id'

    def perform_update(self, serializer):
        serializer.save(date_added=self.request.auth.current_time)
