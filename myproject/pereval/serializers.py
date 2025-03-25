from rest_framework import serializers
from .models import PerevalAdded, Coords, Users, PerevalImages

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'


class PerevalAddedSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coord = CoordsSerializer()
    images = PerevalImagesSerializer(many=True, read_only=True)

    class Meta:
        model = PerevalAdded
        exclude = ['status']


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coord_data = validated_data.pop('coord')
        images_data = validated_data.pop('images', [])

        user = Users.objects.create(**user_data)
        coord = Coords.objects.create(**coord_data)
        pereval = PerevalAdded.objects.create(user=user, coord=coord, **validated_data)

        for image_data in images_data:
            PerevalImages.objects.create(pereval=pereval, **image_data)

        return pereval