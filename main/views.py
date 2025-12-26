from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.views import APIView
from rest_framework.decorators import api_view
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
        except Book.DoesNotExist:
            return Response({"message": "Ma'lumot topilmadi"},status=404)
        return Response(data=dict_to_json(book))
    
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
        except Book.DoesNotExist:
            return Response({"message": "Ma'lumot topilmadi"},status=404)
        
        return Response(data=dict_to_json(book))
    
    def put(self, request: Request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"message": "Ma'lumot topilmadi"},status=404)
        
        data = request.data
        book.name = data.get("name")
        book.author = data.get("author")
        book.year = data.get("year")
        book.price = data.get("price")

        book.save()
        
        return Response(data=dict_to_json(book), status=200)


def dict_to_json(book):
    return {
        "id":book.id,
        "name":book.name,
        "author":book.author,
        "year":book.year,
        "price":book.price
    }


@api_view(['GET'])
def hello(request: Request):
    return Response({"message":"Hello,API!"})

@api_view(['GET'])
def greet(request: Request):
    name = request.query_params.get('name')
    return Response({"message":f"Hello, {name}"})

@api_view(['POST'])
def echo(request: Request):
    data = request.data.get("text")
    return Response({"matn":data})

@api_view(['POST'])
def check_age(request: Request):
    data = request.data.get("age")
    if data < 18:
        return Response({"message":"Access denied"})
    else:
        return Response({"message":"Access granted"})
    
@api_view(['POST'])
def register(request: Request):
    try:
        data = request.data['username']
    except:
        return Response(status=400)
    return Response({"message":f"{data} registered"}, status=201)

@api_view(['GET'])
def square(request: Request, num):
    data = num**2
    return Response({"number":num, "square":data})
    
