from django.db import models

# Create your models here.


class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    TOPIC_ID = 1
    topic = models.ForeignKey(Topic, TOPIC_ID)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.text[:50] + "..."
