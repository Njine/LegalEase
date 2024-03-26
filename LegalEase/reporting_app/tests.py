from django.test import TestCase, Client
from django.urls import reverse
from .models import Report

class ReportingAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a sample report for testing
        self.report = Report.objects.create(
            title='Test Report',
            content='This is a test report content.'
        )

    def test_report_list_view(self):
        # Test accessing the report list view
        response = self.client.get(reverse('report_list'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertContains(response, self.report.title)  # Check if the report title is present in the response content

    def test_report_detail_view(self):
        # Test accessing the report detail view
        response = self.client.get(reverse('report_detail', kwargs={'pk': self.report.pk}))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertContains(response, self.report.title)  # Check if the report title is present in the response content

    # Add more test cases as needed
