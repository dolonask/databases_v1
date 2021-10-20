from rest_framework import serializers

from work.models import GroupOfRights, TradeUnionRight, TradeUnionCrime, Сonvention98, Сonvention87, \
    AntiTradeUnionDiscrimination, СonversationRight, MeetingsRight, ProhibitionOfForcedLabor, FailureSystemicMeasures, \
    ViolationsUsingCompulsoryLabor, GovernmentCoercion, UseOfForcedLabor, Сonvention135, PrincipleOfNonDiscrimination, \
    ConsultationRight, TradeUnionBuildingsRight, ChildLabor, DiscriminationInVariousAreas, DiscriminatiOnVariousGrounds, \
    PublicPolicyDiscrimination, ElectionsRight, CreateStrikeRight, TradeUnionActivityRight, Сonvention138, \
    Сonvention182, Victim
from work.serializers import СonversationRightSerializers, AntiTradeUnionDiscriminationSerializers, \
    TradeUnionCrimeSerializers, MeetingsRightSerializers, ProhibitionOfForcedLaborSerializers, \
    FailureSystemicMeasuresSerializers, ViolationsUsingCompulsoryLaborSerializer, GovernmentCoercionSerializers, \
    UseOfForcedLaborSerializers, Сonvention135Serializers, PrincipleOfNonDiscriminationSerializers, \
    ConsultationRightSerializers, TradeUnionBuildingsRightSerializers, DiscriminationInVariousAreasSerializers, \
    DiscriminatiOnVariousGroundsSerializers, PublicPolicyDiscriminationSerializers, ElectionsRightSerializers, \
    CreateStrikeRightSerializers, TradeUnionActivityRightSerializers, ChildLaborSerializers, Сonvention138Serializers, \
    Сonvention182Serializers, VictimSerializers


# функция для переопределения representation
def get_representation(representation, id, serializer, model):
    if representation.get("id") == id:
        representation['child'] = True
        representation['child_item'] = serializer(model.objects.all(), many=True).data



class ChildLaborSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChildLabor
        fields = ('id', 'name')

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     get_representation(representation, 1, "сonvention138", "О минимальном возрасте для приема на работу",
    #                        Сonvention138Serializers, Сonvention138)
    #     get_representation(representation, 2, "сonvention182", "О запрещении и немедленных мерах по искоренению наихудших форм детского труда",
    #                        Сonvention182Serializers, Сonvention182)
    #     return representation


class DiscriminatiOnVariousGroundsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiscriminatiOnVariousGrounds
        fields = ('id', 'name')

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #
    #     get_representation(representation, 1, "childLabor", "Дискриминация в различных сферах трудовых отношений",
    #                        ChildLaborSerializers, ChildLabor
    #
    #                        )
    #     return representation
# serializer для "дискриминация в различных сферах трудовых отношений"

class PrincipleOfNonDiscriminationSerializers(serializers.ModelSerializer):
    class Meta:
        model = PrincipleOfNonDiscrimination
        fields = ('id', 'name')

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #
    #     get_representation(
    #                         representation, 1, "discriminatiOnVariousGrounds", "Дискриминация по различным основаниям",
    #                         DiscriminatiOnVariousGroundsSerializers, DiscriminatiOnVariousGrounds
    #     )
    #     get_representation(
    #                         representation, 2, "discriminationInVariousAreas", "Дискриминация в различных сферах трудовых отношений",
    #                         DiscriminationInVariousAreasSerializers, DiscriminationInVariousAreas
    #                        )
    #     get_representation(
    #                         representation, 3, "publicPolicyDiscrimination",
    #                         "Нарушения в области проведения государственной политики по искоренению дискриминации и поощрению равенства прав и возможностей",
    #                         PublicPolicyDiscriminationSerializers, PublicPolicyDiscrimination
    #     )
    #     return representation


class TradeUnionRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionRight
        fields = ('id', 'name')
    #

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1,  TradeUnionCrimeSerializers, TradeUnionCrime)
        get_representation(representation, 3, MeetingsRightSerializers, MeetingsRight)
        get_representation(representation, 6, TradeUnionBuildingsRightSerializers, TradeUnionBuildingsRight)
        return representation


class Сonvention87Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention87
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 4, ElectionsRightSerializers, ElectionsRight)
        get_representation(representation, 7, CreateStrikeRightSerializers, CreateStrikeRight)
        get_representation(representation, 5, TradeUnionActivityRightSerializers, TradeUnionActivityRight)
        return representation


class Сonvention98Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention98
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, AntiTradeUnionDiscriminationSerializers, AntiTradeUnionDiscrimination)
        get_representation(representation, 2, СonversationRightSerializers, СonversationRight)
        return representation


class ProhibitionOfForcedLaborSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProhibitionOfForcedLabor
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, UseOfForcedLaborSerializers, UseOfForcedLabor)
        get_representation(representation, 2, "governmentCoercion", "Косвенное принуждение государством к труду",
                            GovernmentCoercionSerializers, GovernmentCoercion
        )
        get_representation(
                            representation, 3, "violationsUsingCompulsoryLabor",
                            "Нарушения при использовании принудительного (обязательного) труда в допустимых случаях",
                            ViolationsUsingCompulsoryLaborSerializer, ViolationsUsingCompulsoryLabor
        )
        get_representation(representation, 4, "failureSystemicMeasures", "Нарушения, связанные с непринятием государством системных мер",
                           FailureSystemicMeasuresSerializers, FailureSystemicMeasures)



        return representation


# группа прав
class GroupOfRightsSerializers(serializers.ModelSerializer):

    class Meta:
        model = GroupOfRights
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, TradeUnionRightSerializers, TradeUnionRight)
        get_representation(representation, 2, Сonvention87Serializers, Сonvention87)
        get_representation(representation, 3, Сonvention98Serializers, Сonvention98)
        get_representation(representation, 4, Сonvention135Serializers, Сonvention135)
        get_representation(representation, 5, ConsultationRightSerializers, ConsultationRight)
        get_representation(representation, 6, PrincipleOfNonDiscriminationSerializers, PrincipleOfNonDiscrimination)
        get_representation(representation, 8, ProhibitionOfForcedLaborSerializers, ProhibitionOfForcedLabor)

        return representation

















# {'id': 'victim', 'name': 'В отношении кого совершено нарушение', 'item': victim.data},
#             {'id': 'intruder', 'name': 'Кем было совершено нарушение', 'item': intruder.data},
#             {'id': 'natureviolation', 'name': 'Характер нарушения', 'item': violation_nature.data},
#             {'id': 'rightsstate', 'name': 'Ситуация с правами', 'item': rights_state.data},
#             {'id': 'victimsituation', 'name': 'Ситуация с потерпевшим(и)', 'item': victim_situation.data},
#             {'id': 'tradeUnionSituation', 'name': 'Профсоюз на месте работы после произошедшего',
#              'item': tradeUnionSituation.data},
#             {'id': 'work_tradeunionactivities', 'name': 'Отрасль деятельности профсоюза', 'item': trade_union_activities.data},
            # {'id': 'user', 'name': 'Монитор', 'item': user.data}
