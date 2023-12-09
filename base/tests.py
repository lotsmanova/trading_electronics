from django.urls import reverse
from rest_framework.test import APITestCase
from trading.models import Product, Contact
from users.models import User


class BaseTestCase(APITestCase):
    """Базовый случай APITestCase"""

    username = 'test_admin'
    password = '12345'

    def setUp(self) -> None:
        self.user = User.objects.create(
            username=self.username
        )

        self.user.set_password(self.password)
        self.user.save()

        response = self.client.post(
            reverse('users:token_obtain_pair'),
            {
                'username': self.username,
                'password': self.password
            }
        )

        self.token = response.json().get('access')

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.product = Product.objects.create(
            name='Test product',
            model='Test1',
            release_date='2023-11-11'
        )

        self.contact = Contact.objects.create(
            email='test@test.ru',
            country='Test country',
            city='Test city',
            street='Test street',
            number_home=2
        )
