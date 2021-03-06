# Generated by Django 3.2.3 on 2021-08-19 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

from main.load.main_dump import load_mains


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('migrant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main.role', verbose_name='Позиция')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='position', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='migrant.country', verbose_name='Страна')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='country', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.RunPython(load_mains)

    ]
