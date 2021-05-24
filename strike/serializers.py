from rest_framework import serializers
from .models import Age, Region


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Age
        fields = '__all__'


class RegionSerializer(serializers.Serializer):
    class Meta:
        model = Region
        fields = '__all__'
