from djoser.conf import User
from rest_framework.response import Response
from rest_framework.views import APIView

from work.serializers import UserSerializers

from work.models import GroupOfRights, Source, Region, Country, Victim, Intruder, NatureViolation, RightsState, \
    TradeUnionSituation, VictimSituation, TradeUnionActivities
from work.serializers import SourceSerializers, CountrySerializers, RegionSerializers, VictimSerializers, \
    IntruderSerializers, NatureViolationSerializers, RightsStateSerializers, TradeUnionSituationSerializers, \
    VictimSituationSerializers, TradeUnionActivitiesSerializers
from work.test_serializers import GroupOfRightsSerializers


class TestDataAPIView(APIView):
    def get(self, request):
        source = SourceSerializers(Source.objects.all(), many=True)
        country = CountrySerializers(Country.objects.all(), many=True)
        region_1 = RegionSerializers(Region.objects.filter(country__pk=1), many=True)
        region_2 = RegionSerializers(Region.objects.filter(country__pk=2), many=True)
        region_3 = RegionSerializers(Region.objects.filter(country__pk=3), many=True)
        region_4 = RegionSerializers(Region.objects.filter(country__pk=4), many=True)
        region_5 = RegionSerializers(Region.objects.filter(country__pk=5), many=True)
        user = UserSerializers(User.objects.all(), many=True)
        victim = VictimSerializers(Victim.objects.all(), many=True)
        intruder = IntruderSerializers(Intruder.objects.all(), many=True)
        violation_nature = NatureViolationSerializers(NatureViolation.objects.all(), many=True)
        rights_state = RightsStateSerializers(RightsState.objects.all(), many=True)
        tradeUnionSituation = TradeUnionSituationSerializers(TradeUnionSituation.objects.all(), many=True)
        victim_situation = VictimSituationSerializers(VictimSituation.objects.all(), many=True)
        trade_union_activities = TradeUnionActivitiesSerializers(TradeUnionActivities.objects.all(), many=True)
        queryset = GroupOfRights.objects.all()
        serializer = GroupOfRightsSerializers(queryset, many=True)
        # print(serializer.data)

        return Response([{"id_name": "groupOfRights", "name": "Группа прав", "item": serializer.data},
                         {'id_name': 'source', 'name': 'Источник информации', 'item': source.data},
                         {'id_name': 'country', 'name': 'Страна', 'item': country.data},
                         {'id_name': 'region', 'name': 'Регион', 'item': {1: region_1.data,
                                                                          2: region_2.data,
                                                                          3: region_3.data,
                                                                          4: region_4.data,
                                                                          5: region_5.data}},
                         {'id_name': 'victim', 'name': 'В отношении кого совершено нарушение', 'item': victim.data},
                         {'id_name': 'intruder', 'name': 'Кем было совершено нарушение', 'item': intruder.data},
                         {'id_name': 'violation_nature', 'name': 'Характер нарушения', 'item': violation_nature.data},
                         {'id_name': 'rights_state', 'name': 'Ситуация с правами', 'item': rights_state.data},
                         {'id_name': 'victim_situation', 'name': 'Ситуация с потерпевшим(и)',
                          'item': victim_situation.data},
                         {'id_name': 'tradeUnionSituation', 'name': 'Профсоюз на месте работы после произошедшего',
                          'item': tradeUnionSituation.data},
                         {'id_name': 'trade_union_activities', 'name': 'Отрасль деятельности профсоюза',
                          'item': trade_union_activities.data},
                         {'id_name': 'user', 'name': 'Монитор', 'item': user.data},
                         ])




#             {'id': 'сonvention138', 'name': 'О минимальном возрасте для приема на работу', 'item': сonvention138.data},
#             {'id': 'convention182',
#              'name': 'О запрещении и немедленных мерах по искоренению наихудших форм детского труда',
#              'item': convention182.data},
