# Generated by Django 3.2.3 on 2021-06-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migrant', '0010_alter_individualinfo_hasagreement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualinfo',
            name='hasAgreement',
            field=models.CharField(choices=[('YES', 'Да'), ('NO', 'Нет')], max_length=20, verbose_name='Был ли подписан трудовой договор?'),
        ),
    ]
