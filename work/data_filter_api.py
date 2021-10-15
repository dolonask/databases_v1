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
        one = get_request_data(request.data)
        two = return_right_data(one)
        # print("two ", two)
        fields = list(two.keys())
        print("two ", fields)
        queryset = Case.objects.filter(**two)
        serializer = DataFilterApiSerializer(queryset, many=True)
        return Response(serializer.data)


