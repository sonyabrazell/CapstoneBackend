from django.db.models import fields
from rest_framework import serializers
from .models import Book, BookTracker

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'cover', 'read_status', 'format', 'genre', 'series', 'special_edition', 'first_edition', 'signed']
        
class BookTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTracker
        fields = ['id', 'title', 'author', 'isbn', 'cover', 'format']
        
class NonTradSerializer(serializers.ModelSerializer):
    pass

class WishlistSerializer(serializers.ModelSerializer):
    pass