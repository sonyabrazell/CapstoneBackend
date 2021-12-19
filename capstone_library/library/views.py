from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Book, BookTracker, OGTracker, Wishlist
from .serializers import BookSerializer, BookTrackerSerializer, OGSerializer, WishlistSerializer


# Create your views here.

# LIBRARY VIEW    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
class BookView(viewsets.ModelViewSet):
    serializer = BookSerializer
    queryset = Book.objects.all()

# BOOK TRACKER VIEW
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
class BookTrackerView(viewsets.ModelViewSet):
    serializer = BookTrackerSerializer
    queryset=BookTracker.objects.all()


# OG TRACKER VIEW
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
class OGTrackerView(viewsets.ModelViewSet):
    serializer = OGSerializer
    queryset=OGTracker.objects.all()

# WISHLIST VIEWS

@api_view(['GET'])
@permission_classes([IsAuthenticated])
class WishlistView(viewsets.ModelViewSet):
    serializer = WishlistSerializer
    queryset = Wishlist.objects.all()