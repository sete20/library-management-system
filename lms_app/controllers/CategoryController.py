from http.client import HTTPResponse
from django.shortcuts import render
from http.client import HTTPResponse
from ..forms import CategoryForm, BookForm
from ..models import Category, Book


def Create(request):
    if request.method == "POST":
        category_add = CategoryForm(request.POST)
        if category_add.is_valid():
            category_add.save()
            category_add = CategoryForm()
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'form': BookForm(),
        'formCat': CategoryForm()
    }
    return render(request, 'pages/index.html', {'context': context})
