# Generated by Django 2.1.7 on 2019-05-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20190520_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpagesettings',
            name='block_aboutus_description',
            field=models.CharField(blank=True, max_length=750, null=True, verbose_name='Описание блока о компании'),
        ),
    ]
