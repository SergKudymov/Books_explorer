from django.shortcuts import render

# Create your views here.


def index(request):
    """ Домашняя страница приложения Books_explorer"""
    return render(request, "books_explorers/index.html")
