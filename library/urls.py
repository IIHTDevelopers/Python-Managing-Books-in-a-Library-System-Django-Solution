from django.urls import path
from library.views import book_list_view

urlpatterns = [
    path('books/', book_list_view, name='book-list'),
]
