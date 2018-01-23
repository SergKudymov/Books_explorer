from django.db import models

# Create your models here.


class Books(models.Model):
    """Тема, которую изучает пользователь"""
    author = models.CharField(max_length=200)
    authors_work = models.CharField(max_length=200)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.authors_work
