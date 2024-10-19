from django.urls import path
from .views import home, CategoryViewSet, ProductViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

# Set up router for the viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', home, name='blog-home'),  # Home view
]

urlpatterns += router.urls  # Add API endpoints to urlpatterns
