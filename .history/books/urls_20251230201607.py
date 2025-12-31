from django.urls import path

from books.views import BookDetailView, BookListView, LibraryDetailView, LibraryListView, ShelfListView

urlpatterns = [
    path('', LibraryListView.as_view(), name = 'libraries'),
    path('shelf', ShelfListView.as_view(), name = 'shelves'),
    path('book', BookListView.as_view(), name="books"),
    path("library-details/<int:pk>", LibraryDetailView.as_view(), name="library.details"),
    path("book-details/<int:pk>", BookDetailView.as_view(), name = "book.details")
    
]