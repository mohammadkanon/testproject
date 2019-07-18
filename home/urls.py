from django.urls import path
from home.views import core, upload, book_list, upload_book

urlpatterns = [
    path('', core, name='core'),
    path('upload/', upload, name='upload'),
    path('books/', book_list, name='book_list'),
    path('books/upload/', upload_book, name='upload_book'),
]