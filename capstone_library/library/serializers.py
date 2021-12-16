from django.db.models import fields
from rest_framework import serializers
from .models import Book, BookTracker, NonTradTracker, Wishlist

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'cover', 'read_status', 'format', 'genre', 'series', 'special_edition', 'first_edition', 'signed']
        
class BookTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTracker
        fields = ['id', 'title', 'author', 'cover', 'date_read']
        
class NonTradSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonTradTracker
        fields = ['id', 'title','author', 'word_count', 'date_read', 'work_link']

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['id', 'title', 'author', 'book_cover']