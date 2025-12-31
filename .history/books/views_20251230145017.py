from django.shortcuts import render
from django.views.generics import ListView

from .models import Library, Shelf, Book

# Create your views here.
class LibraryListView(ListView):
    model = Library
    queryset = Library.objects.all()
    template_name = '/books/library_view.html'
    