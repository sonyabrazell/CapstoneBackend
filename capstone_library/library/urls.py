from django.urls import path
from . import views




urlpatterns = [
    path('books/', views.BookView),
    path('library/', views.UserBooks),
    path('add_new_book/', views.AddUserBooks),
    path('book_tracker/', views.UserReadBooks),
    path('og_tracker/', views.UserReadWork),
    path('book_search', views.BookSearch),
    path('wishlist/', views.UserWishlist),
]
