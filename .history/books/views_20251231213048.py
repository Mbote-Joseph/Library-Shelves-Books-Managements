from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

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
    
class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = "books/library_detailview.html"
    
class ShelfDetailView(DetailView):
    model = Shelf
    context_object_name = 'shelf'
    template_name = 'books/shelf_detailview.html'
    
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detailview.html'
    
class LibraryCreate(CreateView):
    model = Library
    context_object_name = 'library'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    template_name = "books/library_form.html"
    