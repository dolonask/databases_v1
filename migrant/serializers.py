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
class VictimSerializers(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = ('id', 'name')
class BanOnEntrySerializers(serializers.ModelSerializer):
    class Meta:
        model = BanOnEntry
        fields = ('id', 'name')
class InfoSourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = InfoSource
        fields = ('id', 'name')
class RightSerializers(serializers.ModelSerializer):
    class Meta:
        model = Right
        fields = ('id', 'name')
class VictimSerializers(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = ('id', 'name')

class IndividualInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = IndividualInfo
        fields = ('id', 'name')


class IntruderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Intruder
        fields = ('id', 'name')


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EntrepreneurSerializers(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = ('id', 'name')


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


class ViolationTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ViolationType
        fields = ('id', 'name')


class ChangesInSalarySerializers(serializers.ModelSerializer):
    class Meta:
        model = ChangesInSalary
        fields = ('id', 'name')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class MigrantCaseGroupByFilterSerializer(CustomTestSerializer):
    country = serializers.CharField(max_length=256, source="country__name")
    region = serializers.CharField(max_length=256, source="region__name")
    victim = serializers.CharField(max_length=256, source="victim__name")
    banOnEntry = serializers.CharField(max_length=256, source="banOnEntry__name")
    source = serializers.CharField(max_length=256, source="source__name")
    # user = serializers.CharField(max_length=256, source="user__name")
    # entrepreneur = serializers.CharField(max_length=256, source="entrepreneur__entrepreneur_name")
    country_id = serializers.IntegerField()
    victim_id = serializers.IntegerField()
    region_id = serializers.IntegerField()
    banOnEntry_id = serializers.IntegerField()
    source_id = serializers.IntegerField()
    # user_id = serializers.IntegerField()

    class Meta:
        model = Case
        fields = "__all__"