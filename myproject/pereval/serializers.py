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
        extra_kwargs = {'image': {'required': False,  'allow_null': True}}


class PerevalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    images = PerevalImageSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Pereval
        fields = '__all__'
        read_only_fields = ['status', 'add_time']

    def create(self, validated_data):
        request = self.context['request']
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        images_data = validated_data.pop('images', [])

        user, created = User.objects.get_or_create(
            email=user_data['email'],
            defaults=user_data
        )

        coords = Coords.objects.create(**coords_data)

        pereval = Pereval.objects.create(
            user=user,
            coords=coords,
            **validated_data
        )

        images_files = request.FILES

        for field_name, files in images_files.lists():
            if field_name.startswith('images.image'):
                for i, image_file in enumerate(files):
                    title_key = f'images.title[{i}]'
                    title = request.POST.get(title_key, f'Изображение {i + 1}')

                    PerevalImage.objects.create(
                        pereval=pereval,
                        image=image_file,
                        title=title
                    )
        return pereval
