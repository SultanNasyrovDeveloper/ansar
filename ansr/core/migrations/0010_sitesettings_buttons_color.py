# Generated by Django 2.1.7 on 2019-05-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190521_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='buttons_color',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Цвет кнопок'),
        ),
    ]
