# Generated by Django 3.0 on 2021-02-10 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='game_sale',
            field=models.BooleanField(null=True, verbose_name='Скидка'),
        ),
    ]
