from rest_framework import serializers

from work.models import GroupOfRights, TradeUnionRight, TradeUnionCrime, Сonvention98, Сonvention87, \
    AntiTradeUnionDiscrimination


class AntiTradeUnionDiscriminationSerializers(serializers.ModelSerializer):
    class Meta:
        model = AntiTradeUnionDiscrimination
        fields = ('id', 'name')


class TradeUnionRightSerializers(serializers.ModelSerializer):
    class Meta:
        model = TradeUnionRight
        fields = ('id', 'name')


class Сonvention87Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention87
        fields = ('id', 'name')


class Сonvention98Serializers(serializers.ModelSerializer):
    class Meta:
        model = Сonvention98
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get("id") == 1:
            representation['child_item'] = [
                {"id": "antiTradeUnionDiscrimination",
                 "name": "Антипрофсоюзная дискриминация",
                 "child": AntiTradeUnionDiscriminationSerializers(
                     AntiTradeUnionDiscrimination.objects.all(), many=True
                 ).data
                 }]
        return representation




class GroupOfRightsSerializers(serializers.ModelSerializer):

    class Meta:
        model = GroupOfRights
        fields = ('id', 'name')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get("id") == 3:
            representation['child_item'] = [
                { "id" : "сonvention98",
                 "name" : "Нарушения положений Конвенции МОТ №98",
                 "child" : Сonvention98Serializers(
                        Сonvention98.objects.all(), many=True
            ).data
            }]


        print(representation.get("name"))
        # representation['child'] = CategorySerializer(
        #         instance.children.all(), many=True).data
        #     # representation['hi'] = 'hi'

        return representation