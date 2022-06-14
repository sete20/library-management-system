from http.client import HTTPResponse
from django.shortcuts import render
from http.client import HTTPResponse

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def books(request):
    return render(request, 'pages/books.html')
