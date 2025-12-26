from django.urls import path
from .views import *

urlpatterns = [
    path('api/books/', BooksApi.as_view(), name='book'),
    path('api/books/<int:pk>/', One_Book.as_view(), name='book_id'),
    path('api/hello/', hello, name='hello'),
    path('api/greet/', greet, name='greet'),
    path('api/echo/', echo, name='echo'),
    path('api/check-age/', check_age, name='age'),
    path('api/register/', register, name='register'),
    path('api/square/<int:num>/', square, name="kv"),

]