# Generated by Django 3.2.3 on 2021-11-24 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strike', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='strike.card'),
        ),
    ]