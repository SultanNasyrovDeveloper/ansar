# Generated by Django 2.1.7 on 2019-05-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_product_ingrs_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ingrs_file',
            field=models.FileField(blank=True, null=True, upload_to='ingredients/', verbose_name='Файл таблицы ингредиентов'),
        ),
    ]
