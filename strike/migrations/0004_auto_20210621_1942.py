# Generated by Django 3.2.3 on 2021-06-21 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('strike', '0003_cardcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardcomment',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AddField(
            model_name='cardcomment',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 6, 21, 13, 42, 41, 781300, tzinfo=utc), verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]
