
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Book, BookTracker, OGTracker, Wishlist
from .serializers import BookSerializer, BookTrackerSerializer, OGSerializer, WishlistSerializer



# Create your views here.

# LIBRARY VIEW    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def BookView(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
    
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def UserBooks(request):
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        user_books = Book.objects.filter(user_id=request.user.id)
        serializer = BookSerializer(user_books, many=True)
        return Response(serializer.data)   
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteBook(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'DELETE':
        book.delete()
        return Response({'message':'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    

# BOOK TRACKER VIEW
    
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def UserReadBooks(request):
    
    if request.method == 'POST':
        serializer = BookTrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        read_books = BookTracker.objects.filter(user_id=request.user.id)
        serializer = BookTrackerSerializer(read_books, many=True)
        return Response(serializer.data)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteReadBook(request, pk):
    book = BookTracker.objects.get(pk=pk)
    if request.method == 'DELETE':
        book.delete()
        return Response({'message':'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# OG TRACKER VIEW

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def UserReadWork(request):
    
    if request.method == 'POST':
        serializer = OGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        user_read_work = OGTracker.objects.filter(user_id=request.user.id)
        serializer = OGSerializer(user_read_work, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteWork(request, pk):
    book = OGTracker.objects.get(pk=pk)
    if request.method == 'DELETE':
        book.delete()
        return Response({'message':'Work was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# WISHLIST VIEWS

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def UserWishlist(request, pk):
    
    if request.method == 'POST':
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        user_wishlist_book = Wishlist.objects.filter(user_id=request.user.id)
        serializer = WishlistSerializer(user_wishlist_book, many=True)
        return Response(serializer.data)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteWishlistBook(request, pk):
    book = Wishlist.objects.get(pk=pk)
    if request.method == 'DELETE':
        book.delete()
        return Response({'message':'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    