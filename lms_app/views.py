from pprint import pprint
from http.client import HTTPResponse
from django.shortcuts import render
from http.client import HTTPResponse

from .models import Book, Category
from .forms import BookForm, CategoryForm
# Create your views here.


def index(request):
    if request.method == "POST":
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
            add_book = BookForm()
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'form': BookForm(),
        'formCat': CategoryForm
    }
    return render(request, 'pages/index.html', {'context': context})


def books(request):
    books = Book.objects.all()

    return render(request, 'pages/books.html', {'books': books})


def update(request, id):
    if request.method == "POST":
        book_save = BookForm(request.POST, request.FILES,
                             instance=Book.objects.get(id=id))
        if book_save.is_valid():
            book_save.save()
        return render(request, 'pages/update.html', {'book': BookForm(instance=Book.objects.get(id=id))})

    else:
        return render(request, 'pages/update.html', {'book': BookForm(instance=Book.objects.get(id=id))})


def delete(request, id):
    if request.method == "POST":
        Book.objects.filter(id=id).delete()
        context = {
            'books': Book.objects.all(),
            'categories': Category.objects.all(),
            'form': BookForm(),
            'formCat': CategoryForm
        }
        return render(request, 'pages/index.html', {'context': context})
    else:
        return render(request, 'pages/delete.html', {'book': BookForm(instance=Book.objects.get(id=id))})


def search(request, id):

    # return HTTPResponse(request)

    context = {
        'books': Book.objects.filter(categories__id=id),
        'categories': Category.objects.all(),
        'form': BookForm(),
        'formCat': CategoryForm
    }
    return render(request, 'pages/index.html', {'context': context})
