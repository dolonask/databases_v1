# Generated by Django 3.2.3 on 2021-09-08 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_alter_casecomment_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='interval',
            field=models.BooleanField(choices=[(0, 'Точная'), (1, 'Интервал')], default=0, verbose_name='Тип даты нарушения'),
        ),
    ]
