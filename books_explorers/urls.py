"""
Определяет схемы URL для books_explorer.

"""
from django.conf.urls import url
from . import views

app_name = 'books_explorers'
urlpatterns = [
    # Домашняя страница
    url(r'^$', views.index, name='index'),
    # Вывод всех книг
    url(r'books', views.books, name='books')
]
