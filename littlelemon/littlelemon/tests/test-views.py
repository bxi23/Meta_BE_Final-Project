from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        self.menu1 = menu.objects.create(title='Pizza', price=9.99, inventory=100)
        self.menu2 = menu.objects.create(title='Burger', price=5.49, inventory=50)
        self.menu3 = menu.objects.create(title='Pasta', price=7.99, inventory=75)

        self.client = APIClient()
        self.url = reverse('menu-list')

    def test_getall(self):
        # Perform a GET request to the menu endpoint
        response = self.client.get(self.url)

        # Get the serialized data
        expected_data = MenuSerializer(menu.objects.all(), many=True).data

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert the response data matches the serialized data
        self.assertEqual(response.data, expected_data)