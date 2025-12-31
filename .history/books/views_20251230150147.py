from django.shortcuts import render
from django.views.generic import ListView

from .models import Library, Shelf, Book

# Create your views here.
class LibraryListView(ListView):
    model = Library
    context_object_name = "libraries"
    queryset = Library.objects.all()
    template_name = 'books/library_view.html'
    
class ShelfListView(ListView):
    model = Shelf
    context_object_name = "shelves"
    queryset = Shelf.objects.all()
    template_name = 'books/shelf_view.html'
    
    
class BookListView(ListView):
    model = Book
    context_object_name = "books"
    queryset = Book.objects.all()
    template_name = 'books/book_view.html'