from django.urls import path
from . import views



urlpatterns = [
    path('books/', views.BookView.as_view()),
    path('book_tracker/', views.BookTrackerView.as_view()),
    path('og_tracker/', views.OGTrackerView.as_view()),
    path('wishlist/', views.WishlistView.as_view())
]