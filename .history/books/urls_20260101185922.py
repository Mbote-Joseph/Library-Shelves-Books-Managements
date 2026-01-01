from django.urls import path

from books.views import BookDetailView, BookListView, LibraryDetailView, LibraryListView, ShelfCreate, ShelfDetailView, ShelfListView, LibraryCreate

urlpatterns = [
    path('', LibraryListView.as_view(), name = 'libraries'),
    path('libraries', LibraryListView.as_view(), name = 'libraries'),
    path('shelf', ShelfListView.as_view(), name = 'shelves'),
    path('book', BookListView.as_view(), name="books"),
    path("library-details/<int:pk>", LibraryDetailView.as_view(), name="library.details"),
    path('shelf-details/<int:pk>', ShelfDetailView.as_view(), name="shelf.details"),
    path("book-details/<int:pk>", BookDetailView.as_view(), name = "book.details"),
    path('library-create', LibraryCreate.as_view(), name="library.create"),
    path('shelf-create', ShelfCreate.as_view(), name="shelf.create"),
    path('book-create', ShelfCreate.as_view(), name="book.create"),
]