# Generated by Django 3.2.3 on 2021-10-28 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('migrant', '0005_alter_case_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_position_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='migrant.country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='country',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='position',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.role', verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='position',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]