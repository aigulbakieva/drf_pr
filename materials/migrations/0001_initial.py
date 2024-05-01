# Generated by Django 5.0.4 on 2024-05-01 00:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название курса')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='materials/previews', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название урока')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание урока')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='materials/previews', verbose_name='Картинка')),
                ('url', models.URLField(blank=True, null=True, verbose_name='ссылка на видео')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='materials.course', verbose_name='курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
