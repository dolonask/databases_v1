# Generated by Django 3.2.3 on 2021-10-29 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work', '0010_alter_case_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='strike_users', to=settings.AUTH_USER_MODEL, verbose_name='Монитор'),
        ),
    ]
