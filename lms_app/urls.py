from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update')



]
