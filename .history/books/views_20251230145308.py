from django.shortcuts import render
from django.views.generics import ListView

from .models import Library, Shelf, Book

# Create your views here.
class LibraryListView(ListView):
    model = Library
    queryset = Library.objects.all()
    template_name = 'books/library_view.html'
    
class ShelfListView(ListView):
    model = Shelf
    queryset = Shelf.objects.all()
    template_name = 'books/shelf_view.html'
    
    
class BookListView(ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'books/book_view.html'