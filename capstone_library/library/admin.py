from django.contrib import admin
from .models import Book, BookTracker, OGTracker, Wishlist

# Register your models here.

admin.site.register(Book)
admin.site.register(BookTracker)
admin.site.register(OGTracker)
admin.site.register(Wishlist)
