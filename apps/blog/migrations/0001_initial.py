# Generated by Django 3.1.7 on 2021-02-26 09:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CommentPublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Заголовок публикации')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('short_description', models.CharField(max_length=255, verbose_name='Короткое описание')),
                ('description', models.TextField(verbose_name='Описание публикации')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'На модерации'), (1, 'Промодерированно'), (2, 'Отклонено')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='blog.publication')),
            ],
        ),
    ]
