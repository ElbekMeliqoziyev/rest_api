from django.urls import path
from .views import *

urlpatterns = [
    path('api/books/', BooksApi.as_view(), name='book'),
    path('api/books/<int:pk>/', One_Book.as_view(), name='book_id'),
]