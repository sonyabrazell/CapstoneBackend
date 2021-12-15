from django.contrib import admin
from .models import Book, BookGenre, BookFormat

# Register your models here.

admin.site.register(Book)
admin.site.register(BookGenre)
admin.site.register(BookFormat)
