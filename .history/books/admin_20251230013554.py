from django.contrib import admin
from .models import Library, Shelf, Book

# Register your models here.
class LibraryAdminModel(admin.ModelAdmin):
    fields = "__all__"
    list_display = ('name', 'students_capacity', 'location', 'created_on')
    
class ShelfAdminModel(admin.ModelAdmin):
    fields = "__all__"
    
class BookAdminModel(admin.ModelAdmin):
    fields = "__all__"


admin.site.register(Library, LibraryAdminModel)
admin.site.register(Shelf, ShelfAdminModel)
admin.site.register(Book, BookAdminModel)
    