from django.db import models


class SiteSettings(models.Model):
    """ Настройки сайта """
    logo = models.FileField(upload_to='logo/', null=True, blank=True, verbose_name='Логотип')
    # Contacts
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер телефона')
    email = models.CharField(max_length=50, null=True, blank=True, verbose_name='Электронная почта организации')
    site_email = models.CharField(max_length=50, null=True, blank=True, verbose_name='Электронная почта сайта',
                                  help_text='Почта для оповещений с сайта')
    about_us = models.TextField(verbose_name='Текст о нас')
