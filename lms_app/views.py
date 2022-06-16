from http.client import HTTPResponse
from django.shortcuts import render
from http.client import HTTPResponse

from .models import Book, Category

# Create your views here.


def index(request):
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all()
    }
    books = Book.objects.all()
    return render(request, 'pages/index.html', {'context': context})


def books(request):
    books = Book.objects.all()

    return render(request, 'pages/books.html', {'books': books})


def update(request):
    return render(request, 'pages/update.html')


def delete(request):
    return render(request, 'pages/delete.html')
