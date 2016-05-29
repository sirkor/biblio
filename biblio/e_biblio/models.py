from django.db import models
from django.contrib.auth.models import User
import datetime


class Document(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор")
    name = models.CharField(max_length=100, verbose_name="Название")
    format = models.CharField(max_length=8, verbose_name="Формат")
    special = models.CharField(max_length=20, verbose_name="Специальность")
    document_type = models.CharField(max_length=25, verbose_name="Тип")
    document = models.FileField(verbose_name="Файл")
    add_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name="Дата добавления")