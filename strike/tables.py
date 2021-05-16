import django_tables2 as tables
from .models import Card



class CardTable(tables.Table):
    class Meta:
        model = Card
        template_name = "django_tables2/bootstrap.html"
        fields = ("id","added_by","name","country", "region","city_name", "date_create", "date_update")
