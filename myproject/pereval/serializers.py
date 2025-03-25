import base64
from django.core.files.base import ContentFile
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
    image_base64 = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = PerevalImages
        fields = ['id', 'image', 'created_at', 'image_base64']
        extra_kwargs = {
            'image': {'read_only': True},
        }

    def create(self, validated_data):
        image_base64 = validated_data.pop('image_base64', None)
        if image_base64:

            format, imgstr = image_base64.split(';base64,')
            ext = format.split('/')[-1]
            image_data = ContentFile(base64.b64decode(imgstr), name=f'image.{ext}')
            validated_data['image'] = image_data.read()
        return super().create(validated_data)


class PerevalAddedSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coord = CoordsSerializer()
    images = PerevalImagesSerializer(many=True, read_only=False)

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
