# Generated by Django 3.2.3 on 2021-06-02 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migrant', '0002_auto_20210602_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата конца нарушения'),
        ),
    ]