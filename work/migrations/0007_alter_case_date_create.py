# Generated by Django 3.2.3 on 2021-12-28 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_alter_company_tnk_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='date_create',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]