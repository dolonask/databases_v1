from rest_framework import serializers

from work.serializers import CustomTestSerializer
from .models import *
from django.contrib.auth.models import User


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')


class SourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'name')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class DemandCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = DemandCategory
        fields = ('id', 'demand_cat_name')


class EconomicDemandSerializers(serializers.ModelSerializer):
    class Meta:
        model = EconomicDemand
        fields = ('id', 'name')


class PoliticDemandSerializers(serializers.ModelSerializer):
    class Meta:
        model = PoliticDemand
        fields = ('id', 'name')


class ComboDemandSerializers(serializers.ModelSerializer):
    class Meta:
        model = ComboDemand
        fields = ('id', 'name')


class OwnerShipTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = OwnerShipType
        fields = ('id', 'name')


class EmployeesCountSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeesCount
        fields = ('id', 'choice')


class ParticipantsCountSerializers(serializers.ModelSerializer):
    class Meta:
        model = ParticipantsCount
        fields = ('id', 'choice')


class TradeunionChoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeunionChoice
        fields = ('id', 'name')


class InitiatorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Initiator
        fields = ('id', 'name')


class TradeunionDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeunionData
        fields = ('id', 'tradeUnion_name')


class EmployerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'emp_name')


class StrikeCharacterSerializers(serializers.ModelSerializer):
    class Meta:
        model = StrikeCharacter
        fields = ('id', 'name')


class MeetingRequirmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeetingRequirment
        fields = ('id', 'name')


class FilterStrikeGroupSerializer(CustomTestSerializer):
    country = serializers.CharField(max_length=256, source="country__name")
    region = serializers.CharField(max_length=256, source="region__name")
    country_id = serializers.IntegerField()
    region_id = serializers.IntegerField()
    class Meta:
        model = Card
        fields = "__all__"







# class PersonGroupInfoSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = PersonGroupInfo
#         fields = ('id', 'groupCharacter_another')

