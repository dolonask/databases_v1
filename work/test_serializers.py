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
def get_representation(representation, id, id_name, serializer, model):
    if representation.get("id") == id:
        representation['id_name'] = id_name
        representation['child'] = True
        representation['child_item'] = serializer(model.objects.all(), many=True).data


class ChildLaborSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChildLabor
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, "сonvention138", Сonvention138Serializers, Сonvention138)
        get_representation(representation, 2, "сonvention182", Сonvention182Serializers, Сonvention182)
        return representation


class DiscriminatiOnVariousGroundsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiscriminatiOnVariousGrounds
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        get_representation(representation, 1, "childLabor", ChildLaborSerializers, ChildLabor)
        return representation


# serializer для "дискриминация в различных сферах трудовых отношений"

class PrincipleOfNonDiscriminationSerializers(serializers.ModelSerializer):
    class Meta:
        model = PrincipleOfNonDiscrimination
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        get_representation(representation, 1, "discriminatiOnVariousGrounds",
                            DiscriminatiOnVariousGroundsSerializers, DiscriminatiOnVariousGrounds
        )
        get_representation(
                            representation, 2, "discriminationInVariousAreas",
                            DiscriminationInVariousAreasSerializers, DiscriminationInVariousAreas
                           )
        get_representation(representation, 3, "publicPolicyDiscrimination",
                            PublicPolicyDiscriminationSerializers, PublicPolicyDiscrimination
        )
        return representation


class TradeUnionRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionRight
        fields = ('id', 'name')
    #

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, "tradeUnionCrime", TradeUnionCrimeSerializers, TradeUnionCrime)
        get_representation(representation, 3, "meetingsRight",  MeetingsRightSerializers, MeetingsRight)
        get_representation(representation, 6, "tradeUnionBuildingsRight", TradeUnionBuildingsRightSerializers, TradeUnionBuildingsRight)
        return representation


class Сonvention87Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention87
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 4, "electionsRight", ElectionsRightSerializers, ElectionsRight)
        get_representation(representation, 7, "createStrikeRight",  CreateStrikeRightSerializers, CreateStrikeRight)
        get_representation(representation, 5, "tradeUnionActivityRight",  TradeUnionActivityRightSerializers, TradeUnionActivityRight)
        return representation


class Сonvention98Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention98
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, "antiTradeUnionDiscrimination", AntiTradeUnionDiscriminationSerializers, AntiTradeUnionDiscrimination)
        get_representation(representation, 2, "conversationRight", СonversationRightSerializers, СonversationRight)
        return representation


class ProhibitionOfForcedLaborSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProhibitionOfForcedLabor
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, "useOfForcedLabor", UseOfForcedLaborSerializers, UseOfForcedLabor)
        get_representation(representation, 2, "governmentCoercion", GovernmentCoercionSerializers, GovernmentCoercion)
        get_representation(representation, 3, "violationsUsingCompulsoryLabor", ViolationsUsingCompulsoryLaborSerializer, ViolationsUsingCompulsoryLabor)
        get_representation(representation, 4, "failureSystemicMeasures", FailureSystemicMeasuresSerializers, FailureSystemicMeasures)

        return representation


# группа прав
class GroupOfRightsSerializers(serializers.ModelSerializer):

    class Meta:
        model = GroupOfRights
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, "tradeUnionRight", TradeUnionRightSerializers, TradeUnionRight)
        get_representation(representation, 2, "сonvention87",  Сonvention87Serializers, Сonvention87)
        get_representation(representation, 3, "сonvention98", Сonvention98Serializers, Сonvention98)
        get_representation(representation, 4, "сonvention135", Сonvention135Serializers, Сonvention135)
        get_representation(representation, 5, "consultationRight", ConsultationRightSerializers, ConsultationRight)
        get_representation(representation, 6, "principleOfNonDiscrimination", PrincipleOfNonDiscriminationSerializers, PrincipleOfNonDiscrimination)
        get_representation(representation, 8, "prohibitionOfForcedLabor", ProhibitionOfForcedLaborSerializers, ProhibitionOfForcedLabor)

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
