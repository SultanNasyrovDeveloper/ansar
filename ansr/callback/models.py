from django.db import models


class Callback(models.Model):
    name = models.CharField(max_length=70, verbose_name='Имя')
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
