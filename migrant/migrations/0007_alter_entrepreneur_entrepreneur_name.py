# Generated by Django 3.2.3 on 2022-01-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migrant', '0006_auto_20220127_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneur',
            name='entrepreneur_name',
            field=models.CharField(blank=True, help_text='ФИО', max_length=50, verbose_name='ФИО'),
        ),
    ]