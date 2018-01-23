from django.shortcuts import render
# from models import Books
# Create your views here.


def index(request):
    """ Домашняя страница приложения Books_explorer"""
    return render(request, "books_explorers/index.html")


def books(request):
    """ Cтраница со списком авторов """
    # books = Books.objects.create()
    return render(request, "books_explorers/index.html")
