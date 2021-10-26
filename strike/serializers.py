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
    username = serializers.CharField(max_length=256)

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
    added_by = serializers.CharField(max_length=256, source="added_by__username")
    card_demand_categories = serializers.CharField(max_length=256, source="card_demand_categories__demand_cat_name")
    economic_demands = serializers.CharField(max_length=256, source="economic_demands__name")
    meeting_requirements = serializers.CharField(max_length=256, source="meeting_requirements__name")
    meeting_requirements_id = serializers.IntegerField()
    duration = serializers.CharField(max_length=256, source="duration__name")
    employer = serializers.CharField(max_length=256, source="employer__name")
    tradeunion_data = serializers.CharField(max_length=256, source="tradeunion_data__tradeUnion_name")
    initiator = serializers.CharField(max_length=256, source="initiator__name")
    tradeunionChoice = serializers.CharField(max_length=256, source="tradeunionChoice__name")
    company_ownership_type = serializers.CharField(max_length=256, source="company_ownership_type__name")
    count_strike_participants = serializers.CharField(max_length=256, source="count_strike_participants__choice")
    company_employees_count = serializers.CharField(max_length=256, source="company_employees_count__choice")
    card_sources = serializers.CharField(max_length=256, source="card_sources__name")
    combo_demands = serializers.CharField(max_length=256, source="combo_demands__name")
    politic_demands = serializers.CharField(max_length=256, source="politic_demands__name")
    economic_demands = serializers.CharField(max_length=256, source="economic_demands__name")


    company_employees_count_id = serializers.IntegerField()
    count_strike_participants_id = serializers.IntegerField()
    company_ownership_type_id = serializers.IntegerField()
    tradeunionChoice_id = serializers.IntegerField()
    initiator_id = serializers.IntegerField()
    tradeunion_data_id = serializers.IntegerField()
    duration_id = serializers.IntegerField()
    employer_id = serializers.IntegerField()
    added_by_id = serializers.IntegerField()
    country_id = serializers.IntegerField()
    region_id = serializers.IntegerField()
    count = serializers.IntegerField()
    procent = serializers.IntegerField()

    class Meta:
        model = Card
        fields = "__all__"

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if id  == "card_sources":
    #         representation['card_sources'] = SourceSerializers(Source.objects.all(), many=True).data
    #     return representation


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = "__all__"