# Generated by Django 3.2.3 on 2021-09-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migrant', '0003_alter_company_additional'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='date_type',
            field=models.BooleanField(choices=[(0, 'Точная'), (1, 'Интервал')], default=0, verbose_name='Тип даты нарушения'),
        ),
    ]