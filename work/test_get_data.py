from djoser.conf import User
from rest_framework.response import Response
from rest_framework.views import APIView

from migrant.serializers import UserSerializers
from work.models import GroupOfRights
from work.test_functions import GroupOfRightsSerializers


class TestDataAPIView(APIView):
    def get(self, request):

        queryset = GroupOfRights.objects.all()
        serializer = GroupOfRightsSerializers(queryset, many=True)
        return Response(serializer.data)

#
# class DataAPIView(APIView):
#     def get(self, request):
#         source = SourceSerializers(Source.objects.all(), many=True)
#         country = CountrySerializers(Country.objects.all(), many=True)
#         region_1 = RegionSerializers(Region.objects.filter(country__pk=1), many=True)
#         region_2 = RegionSerializers(Region.objects.filter(country__pk=2), many=True)
#         region_3 = RegionSerializers(Region.objects.filter(country__pk=3), many=True)
#         region_4 = RegionSerializers(Region.objects.filter(country__pk=4), many=True)
#         region_5 = RegionSerializers(Region.objects.filter(country__pk=5), many=True)
#         groupOfRights = GroupOfRightsSerializers(GroupOfRights.objects.all(), many=True)
#         tradeUnionRight = TradeUnionRightSerializers(TradeUnionRight.objects.all(), many=True)
#         tradeUnionCrime = TradeUnionCrimeSerializers(TradeUnionCrime.objects.all(), many=True)
#         meetingsRight = MeetingsRightSerializers(MeetingsRight.objects.all(), many=True)
#         сonvention87 = Сonvention87Serializers(Сonvention87.objects.all(), many=True)
#         tradeUnionBuildingsRight = TradeUnionBuildingsRightSerializers(TradeUnionBuildingsRight.objects.all(), many=True)
#         createOrganizationRight = CreateOrganizationRightSerializers(CreateOrganizationRight.objects.all(), many=True)
#         createTradeUnionRight  = CreateTradeUnionRightSerializers(CreateTradeUnionRight.objects.all(), many=True)
#         electionsRight = ElectionsRightSerializers(ElectionsRight.objects.all(), many=True)
#         tradeUnionActivityRight = TradeUnionActivityRightSerializers(TradeUnionActivityRight.objects.all(), many=True)
#         createStrikeRight = CreateStrikeRightSerializers(CreateStrikeRight.objects.all(), many=True)
#         сonvention98 = Сonvention98Serializers(Сonvention98.objects.all(), many=True)
#         antiTradeUnionDiscrimination = AntiTradeUnionDiscriminationSerializers(AntiTradeUnionDiscrimination.objects.all(), many=True)
#         conversationRight = СonversationRightSerializers(СonversationRight.objects.all(), many=True)
#         сonvention135 = Сonvention135Serializers(Сonvention135.objects.all(), many=True)
#         consultationRight = ConsultationRightSerializers(ConsultationRight.objects.all(), many=True)
#         principleOfNonDiscrimination = PrincipleOfNonDiscriminationSerializers(PrincipleOfNonDiscrimination.objects.all(), many=True)
#         discriminatiOnVariousGrounds = DiscriminatiOnVariousGroundsSerializers(DiscriminatiOnVariousGrounds.objects.all(), many=True)
#         discriminationInVariousAreas = DiscriminationInVariousAreasSerializers(DiscriminationInVariousAreas.objects.all(), many=True)
#         publicPolicyDiscrimination  = PublicPolicyDiscriminationSerializers(PublicPolicyDiscrimination.objects.all(), many=True)
#         childLabor = ChildLaborSerializers(ChildLabor.objects.all(), many=True)
#         сonvention138 = Сonvention138Serializers(Сonvention138.objects.all(), many=True)
#         convention182 = Сonvention182Serializers(Сonvention182.objects.all(), many=True)
#         prohibitionOfForcedLabor = ProhibitionOfForcedLaborSerializers(ProhibitionOfForcedLabor.objects.all(), many=True)
#         useOfForcedLabor = UseOfForcedLaborSerializers(UseOfForcedLabor.objects.all(), many=True)
#         governmentCoercion = GovernmentCoercionSerializers(GovernmentCoercion.objects.all(), many=True)
#         violationsUsingCompulsoryLabor = ViolationsUsingCompulsoryLaborSerializer(ViolationsUsingCompulsoryLabor.objects.all(), many=True)
#         failureSystemicMeasures = FailureSystemicMeasuresSerializers(FailureSystemicMeasures.objects.all(), many=True)
#         victim = VictimSerializers(Victim.objects.all(), many=True)
#         intruder = IntruderSerializers(Intruder.objects.all(), many=True)
#         violation_nature = NatureViolationSerializers(NatureViolation.objects.all(), many=True)
#         rights_state = RightsStateSerializers(RightsState.objects.all(), many=True)
#         victim_situation = VictimSituationSerializers(VictimSituation.objects.all(), many=True)
#         tradeUnionSituation = TradeUnionSituationSerializers(TradeUnionSituation.objects.all(), many=True)
#         trade_union_activities = TradeUnionActivitiesSerializers(TradeUnionActivities.objects.all(), many=True)
#         user = UserSerializers(User.objects.all(), many=True)
#
#         # tradeUnionCount = TradeUnionCountSerializers(TradeUnionCount.objects.all(), many=True)
#         # company = CompanySerializers(Company.objects.all(), many=True)
#         # tradeUnionInfo = TradeUnionInfoSerializers(TradeUnionInfo.objects.all(), many=True)
#         # groupOfPersons = GroupOfPersonsSerializers(GroupOfPersons.objects.all(), many=True)
#         # russian_regions = Region.objects.filter()
#         return Response([
#             {'id': 'source', 'name': 'Источник информации', 'item': source.data},
#             {'id': 'country', 'name': 'Страна', 'item': country.data},
#             {'id': 'region', 'name': 'Регион', 'item': {1: region_1.data,
#                                                         2: region_2.data,
#                                                         3: region_3.data,
#                                                         4: region_4.data,
#                                                         5: region_5.data}},
#             {'id': 'groupofrights', 'name': 'Группа прав', 'item': groupOfRights.data},
#             {'id': 'tradeunionright', 'name': 'Нарушение в сфере профсоюзных прав и гражданских свобод',
#              'item': tradeUnionRight.data},
#             {'id': 'tradeunioncrime', 'name': 'Обвинения в преступном поведении в связи с профсоюзной деятельностью',
#              'item': tradeUnionCrime.data},
#             {'id': 'meetingsright', 'name': 'Нарушения права на проведение собраний и демонстраций',
#              'item': meetingsRight.data},
#             {'id': 'сonvention87', 'name': 'Нарушения положений Конвенции МОТ №87', 'item': сonvention87.data},
#             {'id': 'tradeunionbuildingsright', 'name': 'Защита профсоюзных помещений и имущества профсоюзов',
#              'item': tradeUnionBuildingsRight.data},
#             {'id': 'createorganizationright', 'name': 'Создание организации без предварительного разрешения',
#              'item': createOrganizationRight.data},
#             {'id': 'createTradeUnionRight', 'name': 'Создание профсоюзов и вступление в профсоюзы',
#              'item': createTradeUnionRight.data},
#             {'id': 'electionsRight', 'name': 'Нарушение права свободно выбирать своих представителей',
#              'item': electionsRight.data},
#             {'id': 'tradeUnionActivityRight',
#              'name': 'Нарушения права профсоюза организовывать деятельность своего аппарата',
#              'item': tradeUnionActivityRight.data},
#             {'id': 'createStrikeRight', 'name': 'Нарушение права на забастовку', 'item': createStrikeRight.data},
#             {'id': 'сonvention98', 'name': 'Нарушения положений Конвенции МОТ №98', 'item': сonvention98.data},
#             {'id': 'antiTradeUnionDiscrimination', 'name': 'Антипрофсоюзная дискриминация',
#              'item': antiTradeUnionDiscrimination.data},
#             {'id': 'conversationRight', 'name': 'Нарушения права на проведение коллективных переговоров',
#              'item': conversationRight.data},
#             {'id': 'сonvention135', 'name': 'Нарушения положений Конвенции МОТ №135', 'item': сonvention135.data},
#             {'id': 'consultationRight', 'name': 'Проведение консультаций', 'item': consultationRight.data},
#             {'id': 'principleOfNonDiscrimination', 'name': 'Принцип запрещения дискриминации',
#              'item': principleOfNonDiscrimination.data},
#             {'id': 'discriminatiOnVariousGrounds', 'name': 'Дискриминация по различным основаниям',
#              'item': discriminatiOnVariousGrounds.data},
#             {'id': 'discriminationInVariousAreas', 'name': 'Дискриминация в различных сферах трудовых отношений',
#              'item': discriminationInVariousAreas.data},
#             {'id': 'publicPolicyDiscrimination',
#              'name': 'Нарушения в области проведения государственной политики по искоренению дискриминации и поощрению равенства прав и возможностей',
#              'item': publicPolicyDiscrimination.data},
#             {'id': 'childLabor', 'name': 'Дискриминация в различных сферах трудовых отношений',
#              'item': childLabor.data},
#             {'id': 'сonvention138', 'name': 'О минимальном возрасте для приема на работу', 'item': сonvention138.data},
#             {'id': 'convention182',
#              'name': 'О запрещении и немедленных мерах по искоренению наихудших форм детского труда',
#              'item': convention182.data},
#             {'id': 'prohibitionOfForcedLabor', 'name': 'Запрет принудительного труда',
#              'item': prohibitionOfForcedLabor.data},
#             {'id': 'useOfForcedLabor', 'name': 'Использование принудительного труда', 'item': useOfForcedLabor.data},
#             {'id': 'governmentCoercion', 'name': 'Косвенное принуждение государством к труду',
#              'item': governmentCoercion.data},
#             {'id': 'violationsUsingCompulsoryLabor',
#              'name': 'Нарушения при использовании принудительного (обязательного) труда в допустимых случаях',
#              'item': violationsUsingCompulsoryLabor.data},
#             {'id': 'failureSystemicMeasures', 'name': 'Нарушения, связанные с непринятием государством системных мер',
#              'item': failureSystemicMeasures.data},
#             {'id': 'victim', 'name': 'В отношении кого совершено нарушение', 'item': victim.data},
#             {'id': 'intruder', 'name': 'Кем было совершено нарушение', 'item': intruder.data},
#             {'id': 'natureviolation', 'name': 'Характер нарушения', 'item': violation_nature.data},
#             {'id': 'rightsstate', 'name': 'Ситуация с правами', 'item': rights_state.data},
#             {'id': 'victimsituation', 'name': 'Ситуация с потерпевшим(и)', 'item': victim_situation.data},
#             {'id': 'tradeUnionSituation', 'name': 'Профсоюз на месте работы после произошедшего',
#              'item': tradeUnionSituation.data},
#             {'id': 'work_tradeunionactivities', 'name': 'Отрасль деятельности профсоюза', 'item': trade_union_activities.data},
#             {'id': 'user', 'name': 'Монитор', 'item': user.data}
#         ])