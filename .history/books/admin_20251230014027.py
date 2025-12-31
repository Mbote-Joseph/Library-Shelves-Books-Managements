from django.contrib import admin
from .models import Library, Shelf, Book

# Register your models here.
class LibraryAdminModel(admin.ModelAdmin):
    fields =  ('name', 'students_capacity', 'location', 'created_on')
    list_display = ('name', 'students_capacity', 'location', 'created_on')
    
class ShelfAdminModel(admin.ModelAdmin):
    fields = ('label', 'books_capacity', 'library', 'created_on')
    list_display = ('label', 'books_capacity', 'library', 'created_on')
    
class BookAdminModel(admin.ModelAdmin):
    fields = ('title', 'author', 'isbn', 'description', 'is_published', 'is_new', 'shelf')
    list_display = ('title', 'author', 'isbn', 'description', 'is_published', 'is_new', 'shelf')


admin.site.register(Library, LibraryAdminModel)
admin.site.register(Shelf, ShelfAdminModel)
admin.site.register(Book, BookAdminModel)
    