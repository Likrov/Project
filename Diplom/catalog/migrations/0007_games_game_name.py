# Generated by Django 3.0 on 2021-02-11 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20210211_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='game_name',
            field=models.CharField(help_text='Enter field documentation', max_length=100, null=True, verbose_name='Название игры'),
        ),
    ]
