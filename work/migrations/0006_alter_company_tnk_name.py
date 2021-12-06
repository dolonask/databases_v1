# Generated by Django 3.2.3 on 2021-12-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_alter_company_country_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='tnk_name',
            field=models.CharField(blank=True, help_text='Название ТНК, в которую входит эта компания', max_length=100, null=True, verbose_name='Название ТНК, в которую входит эта компания'),
        ),
    ]
