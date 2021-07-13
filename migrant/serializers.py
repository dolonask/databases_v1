from rest_framework import serializers
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

# class PersonGroupSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = PersonGroup
#         fields = ('id', 'name')
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