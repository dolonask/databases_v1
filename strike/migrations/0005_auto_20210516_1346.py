# Generated by Django 3.2.3 on 2021-05-16 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strike', '0004_auto_20210516_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 13, 46, 27, 735618), verbose_name='Дата конца проведения забастовки/акции'),
        ),
        migrations.AlterField(
            model_name='card',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 13, 46, 27, 735618), verbose_name='Дата начало проведения забастовки/акции'),
        ),
    ]
