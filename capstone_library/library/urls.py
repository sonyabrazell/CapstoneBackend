from django.urls import path
from . import views




urlpatterns = [
    path('books/', views.BookView),
    path('library/', views.UserBooks),
    path('library/delete/<int:pk>', views.DeleteBook),
    path('book_tracker/', views.UserReadBooks),
    path('book_tracker/delete/<int:pk>', views.DeleteReadBook),
    path('og_tracker/', views.UserReadWork),
    path('og_tracker/delete/<int:pk>', views.DeleteWork),
    path('wishlist/', views.UserWishlist),
    path('wishlist/delete/<int:pk>', views.DeleteWishlistBook)
]
