from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.views import APIView
from .models import *


class BooksApi(APIView):
    def post(self, request: Request):
        data = request.data
        book = Book.objects.create(
            name = data.get("name"),
            author = data.get("author"),
            price = data.get("price"),
            year = data.get("year")
        )
        book.save()

        return Response(data=dict_to_json(book), status=201)
    
    def get(self, request: Request):
        books = Book.objects.all()
        data = []
        for book in books:
            data.append(dict_to_json(book))
        return Response(data=data)
    
    

class One_Book(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except:
            return Response({"message": "Ma'lumot topilmadi"},status=404)
        return Response(data=dict_to_json(book))
    
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
        except:
            return Response({"message": "Ma'lumot topilmadi"},status=404)
        
        return Response(data=dict_to_json(book))
    
    






def dict_to_json(book):
    return {
        "id":book.id,
        "name":book.name,
        "author":book.author,
        "year":book.year
    }