from django.test import TestCase, Client
from django.urls import reverse
from .models import Case

class CaseAppTestCase(TestCase):
    def setUp(self):
        # Create a test case
        self.case = Case.objects.create(title='Test Case', description='This is a test case')

    def test_case_creation(self):
        # Test creation of a case
        case_count_before = Case.objects.count()
        new_case_data = {
            'title': 'New Case',
            'description': 'This is a new case'
        }
        response = self.client.post(reverse('create_case'), new_case_data)
        self.assertEqual(response.status_code, 302)  # Redirects to case detail page upon successful creation
        self.assertEqual(Case.objects.count(), case_count_before + 1)  # Case count increases by 1

    # Add more test cases for case listing, updating, deleting, etc.

    # Cleanup after tests
    def tearDown(self):
        self.case.delete()
