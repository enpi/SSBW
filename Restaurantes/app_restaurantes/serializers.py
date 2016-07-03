from models import Restaurante
from rest_framework import serializers

class RestaurantSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=500)
    image = serializers.CharField(max_length=500)
    likes = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Restaurante` instance, given the validated data.
        """
        return Restaurante.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Restaurante` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.likes = validated_data.get('likes', instance.likes)

        instance.save()
        return instance