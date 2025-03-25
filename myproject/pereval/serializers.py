from rest_framework import serializers
from .models import User, Coords, Pereval, PerevalImage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']

class PerevalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImage
        fields = ['image', 'title']
        extra_kwargs = {'image': {'required': False}}

class PerevalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    images = PerevalImageSerializer(many=True, required=False)

    class Meta:
        model = Pereval
        fields = '__all__'
        read_only_fields = ['status', 'add_time']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        images_data = validated_data.pop('images', [])

        # Создаем или получаем пользователя
        user, created = User.objects.get_or_create(
            email=user_data['email'],
            defaults=user_data
        )

        # Создаем координаты
        coords = Coords.objects.create(**coords_data)

        # Создаем перевал
        pereval = Pereval.objects.create(
            user=user,
            coords=coords,
            **validated_data
        )

        # Создаем изображения
        for image_data in images_data:
            PerevalImage.objects.create(pereval=pereval, **image_data)

        return pereval