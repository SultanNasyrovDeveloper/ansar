# Generated by Django 2.1.7 on 2019-05-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='badge',
            field=models.CharField(blank=True, default=None, max_length=15, null=True, verbose_name='Бейдж'),
        ),
    ]
