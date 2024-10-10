from rest_framework import generics
from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated


from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the E-commerce API!")



permission_classes = [IsAuthenticated]
class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of products or create a new product.
    """
    queryset = Product.objects.all()  # Get all products from the database
    serializer_class = ProductSerializer  # Use the ProductSerializer for serialization
    permission_classes = [permissions.AllowAny]  # Set permissions for this view

    def perform_create(self, serializer):
        """
        Save the new product instance using the serializer.
        """
        serializer.save()  # Call the save method to create the new product


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a product by its ID.
    """
    queryset = Product.objects.all()  # Get all products from the database
    serializer_class = ProductSerializer  # Use the ProductSerializer for serialization
    permission_classes = [permissions.AllowAny]  # Set permissions for this view

