from django.test import TestCase, Client
from django.urls import reverse

class DatabaseManagerTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_database_view_access(self):
        # Test accessing the database view
        response = self.client.get(reverse('database_view'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response

    # Add more test cases as needed

