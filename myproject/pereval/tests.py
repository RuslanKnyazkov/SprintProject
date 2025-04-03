from django.test import TestCase, Client
from django.urls import reverse

from .models import User, Coords, Pereval


class ModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(name='Иван',
                            fam='Иванов',
                            otc='Иванович',
                            email='ivanov@mail.ru',
                            phone=89030332677)

        coord = Coords.objects.create(latitude =1.45,
                              longitude = 2.66,
                              height = 5000)

        Pereval.objects.create(beauty_title='Красивый горный перевал',
                               title="Горный хребет",
                               user=user,
                               coords = coord)


    def test_check_user_model(self):
        user = User.objects.get(name = 'Иван')
        self.assertEqual([user.name, user.fam, user.otc, user.email, user.phone] ,
                         ['Иван', 'Иванов', 'Иванович', 'ivanov@mail.ru', '89030332677'])
        self.assertEqual(type(user.phone), str)

    def test_check_coord_model(self):
        coord = Coords.objects.get(height = 5000)
        self.assertEqual(coord.height, 5000)


    def test_check_pereval_model(self):
        pereval = Pereval.objects.get(user__name = 'Иван')
        self.assertEqual(pereval.status, 'new')
        pereval.status = 'rejected'
        self.assertEqual(pereval.status, 'rejected')


class ApiClientTestCase(TestCase):

    def setUp(self):
        self.list_url = reverse('pereval-list')

    def test_client_method_get(self):
        responce = self.client.get(self.list_url)
        self.assertEqual(responce.status_code, 200)