from django.urls import path

from books.views import LibraryListView, ShelfListView, BookListView

urlpatterns = [
    path('', LibraryListView.as_view(), name = 'libraries'),
    path('shelf', ShelfListView.as_view(), name = 'shelves'),
    path('book', BookListView.as_view(), name="books")
]