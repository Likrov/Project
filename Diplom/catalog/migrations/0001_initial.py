# Generated by Django 3.0 on 2021-02-10 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(help_text='Enter field documentation', max_length=100, verbose_name='Название игры')),
                ('game_image', models.TextField(blank=True, null=True, verbose_name='Картинка игры')),
                ('game_about', models.TextField(blank=True, null=True, verbose_name='Описание игры')),
                ('game_price', models.FloatField(blank=True, null=True, verbose_name='Цена игры')),
                ('game_valid', models.BooleanField(null=True, verbose_name='Вышла или не вышла игра')),
                ('game_published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавление игры')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-game_name'],
            },
        ),
    ]