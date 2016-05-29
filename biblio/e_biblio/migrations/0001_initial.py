# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('format', models.CharField(max_length=8, verbose_name='Формат')),
                ('special', models.CharField(max_length=20, verbose_name='Специальность')),
                ('document_type', models.CharField(max_length=25, verbose_name='Тип')),
                ('document', models.FileField(upload_to='', verbose_name='Файл')),
                ('add_date', models.DateTimeField(default=datetime.datetime(2016, 5, 29, 15, 55, 46, 553178), verbose_name='Дата добавления')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
