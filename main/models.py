import datetime
#from datetime import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
# создавать новые таблички для БД

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    cur_time = models.DateTimeField(default=timezone.now)

    #вывод объекта на экран
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Reg(models.Model):
    title = models.CharField('Название', max_length=50)
    setup = models.TextField('Установка')
    time = models.TextField('Время')
    task = models.TextField('Задача')
    cur_time = models.DateTimeField(default=timezone.now)

    #вывод объекта на экран
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись на прибор'
        verbose_name_plural = 'Записи на приборы'



