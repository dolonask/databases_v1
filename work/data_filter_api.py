from django.db.models import Count, F
from rest_framework.response import Response
from rest_framework.views import APIView

from work.models import Case
from work.serializers import DataFilterApiSerializer


def get_request_data(request_data):
    dicts = {}
    for i in request_data:
        dicts.update({
            i['id']: i['item']
        })
    return dicts


def return_right_data(custom_dict_data):
    new_json = {}
    item = []
    for i, val in custom_dict_data.items():
        for value in val:
            item.append(int(value['id']))
        new_json.update({
            i: item
     })
        item = list()
    return new_json


class TestDataFilterAPI(APIView):
    def post(self, request):


        #  первая переработка даты
        #  первая переработка даты
        one = get_request_data(request.data)
        #  вторая переработка даты
        two = return_right_data(one)
        dicts = {}
        dicts2 = {}

        country = two.get("country")
        region = two.get("region")
        groupofrights = two.get("groupofrights")
        source = two.get("source")

        fields = list(two.keys())
        print(two)
        if "country" in fields:
            dicts["country__in"] = country
            # dicts["country_id"] = country

        if "region" in fields:
            dicts["region__in"] = region


        if "groupofrights" in fields:
            fields.remove("groupofrights")
            fields.append("groupOfRights")
            dicts["groupOfRights__in"] = groupofrights
            # dicts["groupOfRights_id"] = groupofrights
        if "source" in fields:
            dicts['source__in'] = source
            # dicts['source_id'] = source
        print(dicts)
        fields.append("country_id")

        # поиск по бд
        queryset = Case.objects.filter(**dicts).values("country__name", "country_id", "region__name").annotate(count=Count('id'), procent=100 / Count('id'),)
        # Добавление count и procent
        fields.append("count")
        fields.append("procent")
        print(fields)
        serializer = DataFilterApiSerializer(queryset, many=True, fields=fields)
        return Response(serializer.data)


