# Generated by Django 2.1.7 on 2019-05-15 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190514_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptionParagraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Fat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='fat', to='catalog.Product', verbose_name='Продукт')),
            ],
        ),
        migrations.CreateModel(
            name='Minerals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='minerals', to='catalog.Product', verbose_name='Продукт')),
            ],
        ),
        migrations.CreateModel(
            name='OtherIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='other_ingr', to='catalog.Product', verbose_name='Продукт')),
            ],
        ),
        migrations.CreateModel(
            name='Vitamins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='vitamins', to='catalog.Product', verbose_name='Продукт')),
            ],
        ),
    ]
