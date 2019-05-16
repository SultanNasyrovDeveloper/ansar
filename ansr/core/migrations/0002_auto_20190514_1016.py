# Generated by Django 2.1.7 on 2019-05-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(blank=True, null=True, upload_to='logo/', verbose_name='Логотип')),
            ],
        ),
        migrations.DeleteModel(
            name='IndexPageBanner',
        ),
    ]
