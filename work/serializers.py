from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


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


class GroupOfRightsSerializers(serializers.ModelSerializer):

    class Meta:
        model = GroupOfRights
        fields = ('id', 'name')


class TradeUnionRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionRight
        fields = ('id', 'name')


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


class DiscriminatiOnVariousGroundsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiscriminatiOnVariousGrounds
        fields = ('id', 'name')


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
        fields = ('id', 'name' )


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
    country_ = CountrySerializers(source='name', read_only=True)
    region = serializers.StringRelatedField()
    source = serializers.CharField(max_length=255, read_only=True)
    groupOfRights = serializers.CharField(max_length=255, read_only=True)
    count = serializers.IntegerField()
    procent = serializers.IntegerField()
    country = serializers.CharField(max_length=256)

    class Meta:
        model = Case
        fields = "__all__"
        # fields = ("id", "source", "country", "region", "groupOfRights", "count", "procent")

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['country_'] = 'dghm'
    #     return representation