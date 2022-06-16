# from distutils.text_file import TextFile
# from django.db import models

# # Create your models here.


# class Category():
#     name = models.CharField(max_length=20)
#     books = models.ManyToManyField('Book', related_name='categories')


# class Book(models.Model):
#     title = models.CharField(max_length=20)
#     descripton = models.TextField()
#     categories = models.ManyToManyField(
#         Category, blank=False, related_name='books')
#     photo = models.ImageField(upload_to='photos/%y/%m/%d')


from time import time
from django.db import models

from django import forms
from matplotlib import widgets


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to='users/photos/%y/%m/%d')
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     books = models.ForeignKey('Book', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
#     books = models.ManyToManyField('Book', related_name='books')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    photo = models.ImageField(upload_to='books/photos/%y/%m/%d')
    title = models.CharField(max_length=20)
    descripton = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='categories')
    pagesCount = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ratelPricePerDay = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    ratelPeriod = models.IntegerField(null=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=[
                              ('available', 'available'),
                              ('rental', 'rental'),
                              ('sold', 'sold'),
                              ])

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
