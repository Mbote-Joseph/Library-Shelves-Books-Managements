from django import forms
from .models import Library, Shelf, Book

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ('name', 'students_capacity', 'location')
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control my-1", "placeholder": "Enter the name of the Library"}),
            'students_capacity': forms.TextInput(attrs={"class": "form-control my-1", "placeholder": "Enter the Library students Capacity"}),
            'location': forms.TextInput(attrs={"class": "form-control my-1", "placeholder":"Location of the Library"})
        }
        labels = {
            'name': 'Library Name',
            'students_capacity': 'Number of Students',
            'location': 'Library Location'
        }
        
class ShelfForm(forms.ModelForm):
    class Meta:
        model = Shelf
        fields = ('label', 'books_capacity','library')
        widgets = {
            'label': forms.TextInput(attrs={"class": "form-control my-1", "placeholder": "Shelf Label"}),
            'books_capacity': forms.TextInput(attrs={"class": "form-control my-1", "placeholder": "Total Books Capacity"}),
            'library': forms.TextInput(attrs={"class": "form-control my-1", "placeholder":"Shelf Library"})
        }
        labels = {
            'label': 'Shelf label',
            'books_capacity': 'Number of Books',
            'library': 'Shelf Library'
        }
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author','isbn', 'description', 'shelf')
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control my-1", "placeholder": "Book title"}),
            'author': forms.TextInput(attrs={"class": "form-control my-1", "placeholder": "Authors Name"}),
            'isbn': forms.TextInput(attrs={"class": "form-control my-1", "placeholder":"Book ISBN"}),
            'description': forms.Textarea(attrs={"class": "form-control my-1", "placeholder":"Book Description"}),
            'shelf': forms.Select(attrs={"class": "form-control my-1", "placeholder":"Book ISBN"})
        }
        labels = {
            'label': 'Shelf label',
            'books_capacity': 'Number of Books',
            'library': 'Shelf Library'
        }
        