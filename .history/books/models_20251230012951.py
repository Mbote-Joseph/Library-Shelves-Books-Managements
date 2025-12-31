from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=50)
    students_capacity = models.IntegerField()
    location = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.location}"
    
class Shelf(models.Model):
    label = models.CharField(max_length=50)
    books_capacity = models.CharField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.label} On {self.library} Library"
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=10)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} By {self.author}"