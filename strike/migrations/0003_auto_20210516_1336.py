# Generated by Django 3.2.3 on 2021-05-16 07:36

from django.db import migrations


def load_sources(apps,schema_editor):
    Source = apps.get_model("strike", "Source")
    source = Source(id = 0, name = 'СМИ/Блогер/Лидер мнения', is_active = True)
    source.save()
    source = Source(id = 1, name = 'Работники/участники протеста', is_active = True)
    source.save()
    source = Source(id = 2, name = 'Профсоюз', is_active = True)
    source.save()
    source = Source(id = 3, name = 'Представитель коллектива', is_active = True)
    source.save()
    source = Source(id = 4, name = 'Государственные органы', is_active = True)
    source.save()
    source = Source(id = 5, name = 'Не правительственные организации /гражданские активисты', is_active = True)
    source.save()


class Migration(migrations.Migration):

    dependencies = [
        ('strike', '0002_auto_20210514_1411'),
    ]

    operations = [
        migrations.RunPython(load_sources)
    ]
