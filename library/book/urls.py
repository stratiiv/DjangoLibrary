from django.urls import path
from .views import *
urlpatterns=[
    path('books/',get_books_page,name='books'),
    path('books/<int:id>',get_book_details,name='book-details'),
    path('books/filter',get_filtered_books,name='filter-books'),
    path('books/add',get_add_book,name='add-book')
]