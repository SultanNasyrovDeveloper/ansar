# Generated by Django 2.1.7 on 2019-05-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_indexpagesettings_block_test_background'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexpagesettings',
            name='block_test_background',
        ),
        migrations.AddField(
            model_name='indexpagesettings',
            name='block_aboutus_body',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Текст блока о компании'),
        ),
        migrations.AddField(
            model_name='indexpagesettings',
            name='block_sale_background',
            field=models.FileField(default='', upload_to='test/', verbose_name='Фон блока акция'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpagesettings',
            name='block_sale_subtitle',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Описание блока акция'),
        ),
        migrations.AddField(
            model_name='indexpagesettings',
            name='block_sale_text',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Текст блока акция'),
        ),
        migrations.AddField(
            model_name='indexpagesettings',
            name='block_sale_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название блока акция'),
        ),
        migrations.AlterField(
            model_name='indexpagesettings',
            name='block_aboutus_description',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Описание блока о компании'),
        ),
        migrations.AlterField(
            model_name='indexpagesettings',
            name='block_aboutus_title',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Название блока о компании'),
        ),
    ]
