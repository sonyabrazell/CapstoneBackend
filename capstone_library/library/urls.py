from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.get_all_books.as_view(), name='Library'),
    path('add_new_book/', views.add_new_book.as_view(), name='add_new_book')
    path('delete_book', views.delete_book.as_view())
    path('books_tracker/', views.get_all_read_books.as_view(), name='Book Tracker'),
    path('nontrad_tracker/', views.get_all_read_works.as_view(), name='NonTrad Tracker'),
    path('wishlist/', views.get_all_wishlist_books.as_view(), name='Wishlist')
]