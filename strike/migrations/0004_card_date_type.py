# Generated by Django 3.2.3 on 2021-09-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strike', '0003_auto_20210907_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='date_type',
            field=models.BooleanField(choices=[(0, 'Точная'), (1, 'Интервал')], default=0, verbose_name='Тип даты нарушения'),
        ),
    ]
