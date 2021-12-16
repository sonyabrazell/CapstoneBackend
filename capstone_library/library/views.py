from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Book, BookTracker, NonTradTracker, Wishlist
from .serializers import BookSerializer, BookTrackerSerializer, NonTradSerializer, WishlistSerializer
from django.contrib.auth.models import User

# Create your views here.

client = 'https://openlibrary.org/api/books?bibkeys=`${book_isbn}`&jscmd=data&format=json'

# LIBRARY VIEWS    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, data=request.data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])    
def add_new_book(request):
    if request.method == 'POST':
        book_title = request.POST.get('booktitle')
        book_author = request.POST.get('book_author')
        book_isbn = request.POST.get('book_isbn')
        book_cover = request.POST.get('book_cover')
        read_status = request.POST.get('read_status')
        book_format = request.POST.get('book_format')
        book_genre = request.POST.get('book_genre')
        book_series = request.POST.get('book_series')
        special_edition = request.POST.get('special_edition')
        first_edition = request.POST.get('first_edition')
        signed = request.POST.get('signed')
        new_book = Book(
            book_title=book_title, 
            book_author=book_author, 
            book_isbn=book_isbn,
            book_cover=book_cover,
            read_status=read_status,
            book_format=book_format,
            book_genre=book_genre,
            book_series=book_series,
            special_edition=special_edition,
            first_edition=first_edition,
            signed=signed
            )
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            new_book.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_book(self, pk):
    try:
        return Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404

#get by id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_by_id(self, request, pk):
    book = self.get_book(pk)
    serializer = BookSerializer(book, data=request.data)
    return Response(serializer.data)


#get by title
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_by_title(self, request, title):
    book = self.get_book(title)
    serializer = BookSerializer(book, data=request.data)
    return Response(serializer.data)

#get by isbn
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_by_isbn(self, request, isbn):
    book = self.get_book(isbn)
    serializer = BookSerializer(book, data=request.data)
    return Response(serializer.data)

#delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_book(self, request, pk):
    book = self.get_book(pk)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# BOOK TRACKER VIEWS
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_read_books(request):
    book_read = BookTracker.objects.all()
    serializer = BookTrackerSerializer(book_read, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])    
def add_new_read_book(request):
    if request.method == 'POST':
        tracker_title = request.POST.get('booktitle')
        tracker_author = request.POST.get('book_author')
        tracker_cover = request.POST.get('book_cover')
        book_date_read = request.POST.get('date_read')
        new_read_book = BookTracker(
            tracker_title=tracker_title, 
            tracker_author=tracker_author, 
            tracker_cover=tracker_cover,
            book_date_read=book_date_read
            )
        serializer = BookTrackerSerializer(data=request.data)
        if serializer.is_valid():
            new_read_book.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_read_book(self, pk):
    try:
        return BookTracker.objects.get(pk=pk)
    except BookTracker.DoesNotExist:
        raise Http404
    
#get by id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_read_book_by_id(self, request, pk):
    book_read = self.get_read_book(pk)
    serializer = BookTrackerSerializer(book_read, data=request.data)
    return Response(serializer.data)

#get by isbn
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_read_book_by_isbn(self, request, isbn):
    book_read = self.get_read_book(isbn)
    serializer = BookTrackerSerializer(book_read, data=request.data)
    return Response(serializer.data)

#delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_read_book(self, request, pk):
    book = self.get_read_book(pk)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# NON TRAD TRACKER VIEWS
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_read_works(request):
    works_read = NonTradTracker.objects.all()
    serializer = NonTradSerializer(works_read, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])    
def add_new_read_work(request):
    if request.method == 'POST':
        work_title = request.POST.get('work_title')
        work_author = request.POST.get('work_author')
        word_count = request.POST.get('word_count')
        work_date_read = request.POST.get('date_read')
        work_link = request.POST.get('work_link')
        new_read_work = NonTradTracker(
            work_title=work_title, 
            work_author=work_author, 
            word_count=word_count,
            work_date_read=work_date_read,
            work_link=work_link
            )
        serializer = NonTradSerializer(data=request.data)
        if serializer.is_valid():
            new_read_work.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_read_work(self, pk):
    try:
        return NonTradTracker.objects.get(pk=pk)
    except NonTradTracker.DoesNotExist:
        raise Http404
    
#get by id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_work_by_id(self, request, pk):
    work_read = self.get_read_work(pk)
    serializer = NonTradSerializer(work_read, data=request.data)
    return Response(serializer.data)

#delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_work(self, request, pk):
    work = self.get_read_work(pk)
    work.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# WISHLIST VIEWS

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_wishlist_books(request):
    wishlist_books = Wishlist.objects.all()
    serializer = WishlistSerializer(wishlist_books, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])    
def add_new_wishlist_book(request):
    if request.method == 'POST':
        wishlist_title = request.POST.get('booktitle')
        wishlist_author = request.POST.get('book_author')
        wishlist_cover = request.POST.get('book_cover')
        new_wishlist_book = Wishlist(
            wishlist_title=wishlist_title, 
            wishlist_author=wishlist_author, 
            wishlist_cover=wishlist_cover,
            )
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            new_wishlist_book.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_wishlist_book(self, pk):
    try:
        return Wishlist.objects.get(pk=pk)
    except BookTracker.DoesNotExist:
        raise Http404
    
#get by id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_wishlist_book_by_id(self, request, pk):
    wishlist_book = self.get_wishlist_book(pk)
    serializer = WishlistSerializer(wishlist_book, data=request.data)
    return Response(serializer.data)

#get by isbn
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_wishlist_book_by_isbn(self, request, isbn):
    wishlist_book = self.get_wishlist_book(isbn)
    serializer = BookTrackerSerializer(wishlist_book, data=request.data)
    return Response(serializer.data)

#delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_wishlist_book(self, request, pk):
    wishlist_book = self.get_wishlist_book(pk)
    wishlist_book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

