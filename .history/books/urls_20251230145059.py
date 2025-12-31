from django.urls import path

from books.views import LibraryListView

urlpatterns = [
    path('', LibraryListView.as_view(), name = 'libraries')
]