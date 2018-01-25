from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .parsers.link_parser import gen_links
from .models import Author, Book
from .common.http_helper import get_authors_url
# from models import Books
# Create your views here.


def index(request):
    """ Домашняя страница приложения Books_explorer"""
    return render(request, "books_explorers/index.html")


@login_required
def authors(request):
    """ Cтраница со списком авторов """
    authors_url = get_authors_url()
    authors_links = gen_links(authors_url)

    for author in authors_links:
        if author not in Author.objects.values_list('author_name', flat=True):
            Author.objects.create(author_name=author)

    authors_names = Author.objects.values_list(
        'author_name', flat=True).distinct()

    contex = {'authors_names': authors_names}

    return render(request, "books_explorers/authors.html", contex)


def books(request, author_name):
    """ Cтраница с данными расчётов по книгам """
    authors_url = get_authors_url()
    books_url = authors_url + author_name
    books_links = gen_links(books_url)

    for book in books_links:
        if book not in Book.objects.values_list('book_name', flat=True):
            Book.objects.create(author_name=author_name, book_name=book)

    return render(request, "books_explorers/books.html")


def login(request):
    """ Cтраница входа """
    return render(request, "books_explorers/login.html")


def logout(request):
    """ Выход """
    return render(request, "books_explorers/logout.html")
