from rest_framework import serializers

from migrant.models import Case as MigrantCase
from strike.models import Card
from work.models import Case as WorkCase
from work.models import Country


class MigrantResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = MigrantCase
        fields = "__all__"

class WorkResultSerializer(serializers.ModelSerializer):
    country = serializers.CharField()
    class Meta:
        model = WorkCase
        fields = "__all__"

class StrikeResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = "__all__"
