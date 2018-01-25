from django.db import models

# Create your models here.


class Book(models.Model):
    author_name = models.ForeignKey('Author', on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.authors_work


class Author(models.Model):
    """Автор книги"""
    author_name = models.CharField(max_length=200)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.author_name
