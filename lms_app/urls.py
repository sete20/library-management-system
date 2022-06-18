from django.urls import path, include
from . import views
from .controllers import CategoryController
urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('create_category', CategoryController.Create, name="create_category"),
    path('book/search/<int:id>', views.search, name='search_by_category')

]
