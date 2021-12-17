from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.get_all_books.as_view()),
    path('add_new_book/', views.add_new_book.as_view()),
    path('delete_book', views.delete_book.as_view()),
    path('book_tracker/', views.get_all_read_books.as_view()),
    path('og_tracker/', views.get_all_read_works.as_view()),
    path('wishlist/', views.get_all_wishlist_books.as_view())
]