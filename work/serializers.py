from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
# функция для переопределения representation
def get_representation(representation, id, id_name, serializer, model):
    if representation.get("id") == id:
        representation['id_name'] = id_name
        representation['child'] = True
        representation['item'] = serializer(model.objects.all(), many=True).data
class SourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'name')
class CaseSer(serializers.Serializer):
    class Meta:
        # model = Case
        fields = ('case_name', 'source')
class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')
class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')
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
class TradeUnionCrimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionCrime
        fields = ('id', 'name')
class MeetingsRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeetingsRight
        fields = ('id', 'name')
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
class TradeUnionBuildingsRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionBuildingsRight
        fields = ('id', 'name')
class CreateOrganizationRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = CreateOrganizationRight
        fields = ('id', 'name')
class CreateTradeUnionRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = CreateTradeUnionRight
        fields = ('id', 'name')
class ElectionsRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = ElectionsRight
        fields = ('id', 'name')
class TradeUnionActivityRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionActivityRight
        fields = ('id', 'name')
class CreateStrikeRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = CreateStrikeRight
        fields = ('id', 'name')
class Сonvention98Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention98
        fields = ('id', 'name')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, "antiTradeUnionDiscrimination", AntiTradeUnionDiscriminationSerializers, AntiTradeUnionDiscrimination)
        get_representation(representation, 2, "conversationRight", СonversationRightSerializers, СonversationRight)
        return representation
class AntiTradeUnionDiscriminationSerializers(serializers.ModelSerializer):
    class Meta:
        model = AntiTradeUnionDiscrimination
        fields = ('id', 'name')
class СonversationRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = СonversationRight
        fields = ('id', 'name')
class Сonvention135Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention135
        fields = ('id', 'name')
class ConsultationRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConsultationRight
        fields = ('id', 'name')
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
class DiscriminatiOnVariousGroundsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiscriminatiOnVariousGrounds
        fields = ('id', 'name')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, "childLabor", ChildLaborSerializers, ChildLabor)
        return representation
class DiscriminationInVariousAreasSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiscriminationInVariousAreas
        fields = ('id', 'name')
class PublicPolicyDiscriminationSerializers(serializers.ModelSerializer):
    class Meta:
        model = PublicPolicyDiscrimination
        fields = ('id', 'name')
class ChildLaborSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChildLabor
        fields = ('id', 'name')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, "сonvention138", Сonvention138Serializers, Сonvention138)
        get_representation(representation, 2, "сonvention182", Сonvention182Serializers, Сonvention182)
        return representation
class Сonvention138Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention138
        fields = ('id', 'name')
class Сonvention182Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention182
        fields = ('id', 'name')
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
class UseOfForcedLaborSerializers(serializers.ModelSerializer):
    class Meta:
        model = UseOfForcedLabor
        fields = ('id', 'name')
class GovernmentCoercionSerializers(serializers.ModelSerializer):
    class Meta:
        model = GovernmentCoercion
        fields = ('id', 'name')
class ViolationsUsingCompulsoryLaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViolationsUsingCompulsoryLabor
        fields = ('id', 'name')
class FailureSystemicMeasuresSerializers(serializers.ModelSerializer):
    class Meta:
        model = FailureSystemicMeasures
        fields = ('id', 'name')
class VictimSerializers(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = ('id', 'name')
class TradeUnionInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionInfo
        fields = '__all__'
class GroupOfPersonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupOfPersons
        fields = '__all__'
class IntruderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Intruder
        fields = ('id', 'name')
class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
class NatureViolationSerializers(serializers.ModelSerializer):
    class Meta:
        model = NatureViolation
        fields = ('id', 'name')
class RightsStateSerializers(serializers.ModelSerializer):
    class Meta:
        model = RightsState
        fields = ('id', 'name')
class VictimSituationSerializers(serializers.ModelSerializer):
    class Meta:
        model = VictimSituation
        fields = ('id', 'name')
class TradeUnionSituationSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionSituation
        fields = ('id', 'name')
class TradeUnionCountSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionCount
        fields = '__all__'
class UserSerializers(serializers.ModelSerializer):
    name = serializers.CharField(source='username')
    class Meta:
        model = User
        fields = ('id', 'name')
class TradeUnionActivitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionActivities
        fields = ('id', 'name')
class CustomTestSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        # Instantiate the superclass normally
        super(CustomTestSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
class DataFilterApiSerializer(CustomTestSerializer):
    country = serializers.CharField(max_length=255, read_only=True, source='country__name')
    region = serializers.CharField(max_length=255, read_only=True, source='region__name')
    source = serializers.CharField(max_length=255, read_only=True, source='source__name')
    groupOfRights = serializers.CharField(max_length=255, read_only=True, source='groupOfRights__name')
    tradeUnionRight = serializers.CharField(max_length=255, read_only=True, source='tradeUnionRight__name')
    tradeUnionCrime = serializers.CharField(max_length=255, read_only=True, source='tradeUnionCrime__name')
    trade_union_activities = serializers.CharField(max_length=255, read_only=True, source='trade_union_activities__name')
    user = serializers.CharField(max_length=255, read_only=True, source="user__username")
    victim = serializers.CharField(max_length=255, read_only=True, source='victim__name')
    start_date = serializers.CharField(max_length=255, read_only=True)
    count = serializers.IntegerField()
    procent = serializers.IntegerField()
    country_id = serializers.IntegerField()
    region_id = serializers.IntegerField()
    groupOfRights_id = serializers.IntegerField()
    source_id = serializers.IntegerField(source='source__id')
    tradeUnionRight_id = serializers.IntegerField()
    tradeUnionCrime_id = serializers.IntegerField()
    meetingsRight_id = serializers.IntegerField()
    сonvention87_id = serializers.IntegerField()
    tradeUnionBuildingsRight_id = serializers.IntegerField()
    createOrganizationRight_id = serializers.IntegerField()
    createTradeUnionRight_id = serializers.IntegerField()
    electionsRight_id = serializers.IntegerField()
    tradeUnionActivityRight_id = serializers.IntegerField()
    сonversationRight_id = serializers.IntegerField()
    createStrikeRight_id = serializers.IntegerField()
    сonvention98_id = serializers.IntegerField()
    antiTradeUnionDiscrimination_id = serializers.IntegerField()
    сonvention135_id = serializers.IntegerField()
    consultationRight_id = serializers.IntegerField()
    principleOfNonDiscrimination_id = serializers.IntegerField()
    discriminatiOnVariousGrounds_id = serializers.IntegerField()
    discriminationInVariousAreas_id = serializers.IntegerField()
    publicPolicyDiscrimination_id = serializers.IntegerField()
    childLabor_id = serializers.IntegerField()
    сonvention138_id = serializers.IntegerField()
    сonvention182_id = serializers.IntegerField()
    prohibitionOfForcedLabor_id = serializers.IntegerField()
    useOfForcedLabor_id = serializers.IntegerField()
    governmentCoercion_id = serializers.IntegerField()
    violationsUsingCompulsoryLabor_id = serializers.IntegerField()
    failureSystemicMeasures_id = serializers.IntegerField()
    violation_nature_id = serializers.IntegerField()
    rights_state_id = serializers.IntegerField()
    victim_situation_id = serializers.IntegerField()
    tradeUnionSituation_id = serializers.IntegerField()
    trade_union_activities_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    victim_id = serializers.IntegerField()
    intruder_id = serializers.IntegerField(source='intruder__id')
    class Meta:
        model = Case
        fields = "__all__"


from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
# функция для переопределения representation
def get_representation(representation, id, id_name, serializer, model):
    if representation.get("id") == id:
        representation['id_name'] = id_name
        representation['child'] = True
        representation['item'] = serializer(model.objects.all(), many=True).data
class SourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'name')
class CaseSer(serializers.Serializer):
    class Meta:
        # model = Case
        fields = ('case_name', 'source')
class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')
class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')
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
class TradeUnionCrimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionCrime
        fields = ('id', 'name')
class MeetingsRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeetingsRight
        fields = ('id', 'name')
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
class TradeUnionBuildingsRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionBuildingsRight
        fields = ('id', 'name')
class CreateOrganizationRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = CreateOrganizationRight
        fields = ('id', 'name')
class CreateTradeUnionRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = CreateTradeUnionRight
        fields = ('id', 'name')
class ElectionsRightSerializers(serializers.
ModelSerializer):
    class Meta:
        model = ElectionsRight
        fields = ('id', 'name')
class TradeUnionActivityRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionActivityRight
        fields = ('id', 'name')
class CreateStrikeRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = CreateStrikeRight
        fields = ('id', 'name')
class Сonvention98Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention98
        fields = ('id', 'name')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, "antiTradeUnionDiscrimination", AntiTradeUnionDiscriminationSerializers, AntiTradeUnionDiscrimination)
        get_representation(representation, 2, "conversationRight", СonversationRightSerializers, СonversationRight)
        return representation
class AntiTradeUnionDiscriminationSerializers(serializers.ModelSerializer):
    class Meta:
        model = AntiTradeUnionDiscrimination
        fields = ('id', 'name')
class СonversationRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = СonversationRight
        fields = ('id', 'name')
class Сonvention135Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention135
        fields = ('id', 'name')
class ConsultationRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConsultationRight
        fields = ('id', 'name')
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
class DiscriminatiOnVariousGroundsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiscriminatiOnVariousGrounds
        fields = ('id', 'name')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, "childLabor", ChildLaborSerializers, ChildLabor)
        return representation
class DiscriminationInVariousAreasSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiscriminationInVariousAreas
        fields = ('id', 'name')
class PublicPolicyDiscriminationSerializers(serializers.ModelSerializer):
    class Meta:
        model = PublicPolicyDiscrimination
        fields = ('id', 'name')
class ChildLaborSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChildLabor
        fields = ('id', 'name')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        get_representation(representation, 1, "сonvention138", Сonvention138Serializers, Сonvention138)
        get_representation(representation, 2, "сonvention182", Сonvention182Serializers, Сonvention182)
        return representation
class Сonvention138Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention138
        fields = ('id', 'name')
class Сonvention182Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention182
        fields = ('id', 'name')
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

class UseOfForcedLaborSerializers(serializers.ModelSerializer):
    class Meta:
        model = UseOfForcedLabor
        fields = ('id', 'name')
class GovernmentCoercionSerializers(serializers.ModelSerializer):
    class Meta:
        model = GovernmentCoercion
        fields = ('id', 'name')
class ViolationsUsingCompulsoryLaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViolationsUsingCompulsoryLabor
        fields = ('id', 'name')
class FailureSystemicMeasuresSerializers(serializers.ModelSerializer):
    class Meta:
        model = FailureSystemicMeasures
        fields = ('id', 'name')
class VictimSerializers(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = ('id', 'name')
class TradeUnionInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionInfo
        fields = '__all__'
class GroupOfPersonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupOfPersons
        fields = '__all__'
class IntruderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Intruder
        fields = ('id', 'name')
class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
class NatureViolationSerializers(serializers.ModelSerializer):
    class Meta:
        model = NatureViolation
        fields = ('id', 'name')
class RightsStateSerializers(serializers.ModelSerializer):
    class Meta:
        model = RightsState
        fields = ('id', 'name')
class VictimSituationSerializers(serializers.ModelSerializer):
    class Meta:
        model = VictimSituation
        fields = ('id', 'name')
class TradeUnionSituationSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionSituation
        fields = ('id', 'name')
class TradeUnionCountSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionCount
        fields = '__all__'
class UserSerializers(serializers.ModelSerializer):
    name = serializers.CharField(source='username')
    class Meta:
        model = User
        fields = ('id', 'name')
class TradeUnionActivitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionActivities
        fields = ('id', 'name')
class CustomTestSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        # Instantiate the superclass normally
        super(CustomTestSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class DataFilterApiSerializer(CustomTestSerializer):
    country = serializers.CharField(max_length=255, read_only=True, source='country__name')
    region = serializers.CharField(max_length=255, read_only=True, source='region__name')
    source = serializers.CharField(max_length=255, read_only=True, source='source__name')
    groupOfRights = serializers.CharField(max_length=255, read_only=True, source='groupOfRights__name')
    tradeUnionRight = serializers.CharField(max_length=255, read_only=True, source='tradeUnionRight__name')
    tradeUnionCrime = serializers.CharField(max_length=255, read_only=True, source='tradeUnionCrime__name')
    meetingsRight = serializers.CharField(max_length=255, read_only=True, source='meetingsRight__name')
    сonvention87 = serializers.CharField(max_length=255, read_only=True, source='сonvention87__name')
    tradeUnionBuildingsRight = serializers.CharField(max_length=255, read_only=True,
                                                     source='tradeUnionBuildingsRight__name')
    createOrganizationRight = serializers.CharField(max_length=255, read_only=True,
                                                    source='createOrganizationRight__name')
    createTradeUnionRight = serializers.CharField(max_length=255, read_only=True, source='createTradeUnionRight__name')
    electionsRight = serializers.CharField(max_length=255, read_only=True, source='electionsRight__name')
    tradeUnionActivityRight = serializers.CharField(max_length=255, read_only=True,
                                                    source='tradeUnionActivityRight__name')
    сonversationRight = serializers.CharField(max_length=255, read_only=True, source='сonversationRight__name')
    createStrikeRight = serializers.CharField(max_length=255, read_only=True, source='createStrikeRight__name')
    сonvention98 = serializers.CharField(max_length=255, read_only=True, source='сonvention98__name')
    antiTradeUnionDiscrimination = serializers.CharField(max_length=255, read_only=True,
                                                         source='antiTradeUnionDiscrimination__name')
    сonvention135 = serializers.CharField(max_length=255, read_only=True, source='сonvention135__name')
    consultationRight = serializers.CharField(max_length=255, read_only=True, source='consultationRight__name')
    principleOfNonDiscrimination = serializers.CharField(max_length=255, read_only=True,
                                                         source='principleOfNonDiscrimination__name')
    discriminatiOnVariousGrounds = serializers.CharField(max_length=255, read_only=True,
                                                         source='discriminatiOnVariousGrounds__name')
    discriminationInVariousAreas = serializers.CharField(max_length=255, read_only=True,
                                                         source='discriminationInVariousAreas__name')
    publicPolicyDiscrimination = serializers.CharField(max_length=255, read_only=True,
                                                       source='publicPolicyDiscrimination__name')
    childLabor = serializers.CharField(max_length=255, read_only=True, source='childLabor__name')
    сonvention138 = serializers.CharField(max_length=255, read_only=True, source='сonvention138__name')
    сonvention182 = serializers.CharField(max_length=255, read_only=True, source='сonvention182__name')
    prohibitionOfForcedLabor = serializers.CharField(max_length=255, read_only=True,
                                                     source='prohibitionOfForcedLabor__name')
    useOfForcedLabor = serializers.CharField(max_length=255, read_only=True, source='useOfForcedLabor__name')
    governmentCoercion = serializers.CharField(max_length=255, read_only=True, source='governmentCoercion__name')
    violationsUsingCompulsoryLabor = serializers.CharField(max_length=255, read_only=True,
                                                           source='violationsUsingCompulsoryLabor__name')
    failureSystemicMeasures = serializers.CharField(max_length=255, read_only=True,
                                                    source='failureSystemicMeasures__name')
    intruder = serializers.CharField(max_length=255, read_only=True, source='intruder__name')
    violation_nature = serializers.CharField(max_length=255, read_only=True, source='violation_nature__name')
    rights_state = serializers.CharField(max_length=255, read_only=True, source='rights_state__name')
    victim_situation = serializers.CharField(max_length=255, read_only=True, source='victim_situation__name')
    tradeUnionSituation = serializers.CharField(max_length=255, read_only=True, source='tradeUnionSituation__name')
    trade_union_activities = serializers.CharField(max_length=255, read_only=True, source='trade_union_activities__name')
    user = serializers.CharField(max_length=255, read_only=True, source="user__username")
    victim = serializers.CharField(max_length=255, read_only=True, source='victim__name')
    start_date = serializers.CharField(max_length=255, read_only=True)
    count = serializers.IntegerField()
    procent = serializers.IntegerField()
    country_id = serializers.IntegerField()
    region_id = serializers.IntegerField()
    groupOfRights_id = serializers.IntegerField()
    source_id = serializers.IntegerField(source='source__id')
    tradeUnionRight_id = serializers.IntegerField()
    tradeUnionCrime_id = serializers.IntegerField()
    meetingsRight_id = serializers.IntegerField()
    сonvention87_id = serializers.IntegerField()
    tradeUnionBuildingsRight_id = serializers.IntegerField()
    createOrganizationRight_id = serializers.IntegerField()
    createTradeUnionRight_id = serializers.IntegerField()
    electionsRight_id = serializers.IntegerField()
    tradeUnionActivityRight_id = serializers.IntegerField()
    сonversationRight_id = serializers.IntegerField()
    createStrikeRight_id = serializers.IntegerField()
    сonvention98_id = serializers.IntegerField()
    antiTradeUnionDiscrimination_id = serializers.IntegerField()
    сonvention135_id = serializers.IntegerField()
    consultationRight_id = serializers.IntegerField()
    principleOfNonDiscrimination_id = serializers.IntegerField()
    discriminatiOnVariousGrounds_id = serializers.IntegerField()
    discriminationInVariousAreas_id = serializers.IntegerField()
    publicPolicyDiscrimination_id = serializers.IntegerField()
    childLabor_id = serializers.IntegerField()
    сonvention138_id = serializers.IntegerField()
    сonvention182_id = serializers.IntegerField()
    prohibitionOfForcedLabor_id = serializers.IntegerField()
    useOfForcedLabor_id = serializers.IntegerField()
    governmentCoercion_id = serializers.IntegerField()
    violationsUsingCompulsoryLabor_id = serializers.IntegerField()
    failureSystemicMeasures_id = serializers.IntegerField()
    violation_nature_id = serializers.IntegerField()
    rights_state_id = serializers.IntegerField()
    victim_situation_id = serializers.IntegerField()
    tradeUnionSituation_id = serializers.IntegerField()
    trade_union_activities_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    victim_id = serializers.IntegerField()
    intruder_id = serializers.IntegerField(source='intruder__id')

    class Meta:
        model = Case
        fields = "__all__"
