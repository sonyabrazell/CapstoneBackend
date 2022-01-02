from django.db.models import fields
from rest_framework import serializers
from .models import Book, BookTracker, OGTracker, Wishlist

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_title', 'book_author', 'book_isbn', 'book_cover', 'read_status', 'date_read', 'book_format', 'book_genre', 'book_series', 'series_name', 'special_edition', 'first_edition', 'signed']
        
class BookTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTracker
        fields = ['id', 'book_title', 'book_author', 'book_cover', 'date_read']
        
class OGSerializer(serializers.ModelSerializer):
    class Meta:
        model = OGTracker
        fields = ['id', 'work_title','work_author', 'word_count', 'work_date_read', 'work_link']

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['id', 'book_title', 'book_author', 'book_cover']