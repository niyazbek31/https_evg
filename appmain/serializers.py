from rest_framework import serializers

from .models import Pizza

'''
    Serializers (Сериализаторы) позволяют преобразовывать сложные данные, такие как наборы запросов querysets 
    и объекты моделей, в типы данных Python, которые затем можно легко преобразовать в JSON, XML или другие content types.
'''

class PizzaSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    price = serializers.FloatField()

    #
    def create(self, validated_data):
        return Pizza.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
