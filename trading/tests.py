from rest_framework import status

from base.tests import BaseTestCase
from trading.models import NetworkNode


class TradingTestCase(BaseTestCase):
    """Тестирование CRUD NetworkNode"""

    def setUp(self) -> None:
        super().setUp()

        self.node_network = NetworkNode.objects.create(
            name='Test name',
            contact=self.contact
        )
        self.node_network.products.add(self.product.pk)

    def test_create_node_network(self):
        """Тестирование создания объекта сети"""

        data = {
            'name': 'Test factory',
            'contact': self.contact.pk,
            'products': [self.product.pk]
        }

        response = self.client.post(
            '/trading/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json()['name'],
            'Test factory'
        )

    def test_list_node_network(self):
        """Тестирование вывода списка объекта сети"""

        response = self.client.get(
            '/trading/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.json()),
            1
        )

    def test_retrieve_node_network(self):
        """Тестирование вывода объекта сети"""

        response = self.client.get(
            f'/trading/{self.node_network.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['name'],
            'Test name'
        )

    def test_update_node_network(self):
        """Тестирование обновления объекта сети"""

        data = {'name': 'Test update'}

        response = self.client.patch(
            f'/trading/{self.node_network.pk}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['name'],
            'Test update'
        )

    def test_delete_node_network(self):
        """Тестирование удаления объекта сети"""

        response = self.client.delete(
            f'/trading/{self.node_network.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
