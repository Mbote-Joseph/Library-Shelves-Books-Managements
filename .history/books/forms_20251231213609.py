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