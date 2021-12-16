from django.contrib import admin
from .models import Book, BookTracker, NonTradTracker, Wishlist

# Register your models here.

admin.site.register(Book)
admin.site.register(BookTracker)
admin.site.register(NonTradTracker)
admin.site.register(Wishlist)
