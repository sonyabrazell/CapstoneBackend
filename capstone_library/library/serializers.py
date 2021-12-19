from django.db.models import fields
from rest_framework import serializers
from .models import Book, BookTracker, OGTracker, Wishlist

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'cover', 'read_status', 'format', 'genre', 'series', 'special_edition', 'first_edition', 'signed']
        
class BookTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTracker
        fields = ['id', 'title', 'author', 'cover', 'date_read']
        
class OGSerializer(serializers.ModelSerializer):
    class Meta:
        model = OGTracker
        fields = ['id', 'title','author', 'word_count', 'date_read', 'work_link']

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['id', 'title', 'author', 'cover']