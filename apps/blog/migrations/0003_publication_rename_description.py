# Generated by Django 3.1.7 on 2021-02-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210226_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='description',
        ),
        migrations.AddField(
            model_name='publication',
            name='text',
            field=models.TextField(default='', verbose_name='Содержание'),
            preserve_default=False,
        ),
    ]