# Generated by Django 2.1.7 on 2019-05-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_sitesettings_about_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='font1',
            field=models.FileField(default='', upload_to='fonts/', verbose_name='Шрифт 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='font2',
            field=models.FileField(default='', upload_to='fonts/', verbose_name='Шрифт 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='font3',
            field=models.FileField(default='', upload_to='fonts/', verbose_name='Шрифт 3'),
            preserve_default=False,
        ),
    ]
