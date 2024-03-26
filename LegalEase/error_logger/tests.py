from django.test import TestCase, Client
from django.urls import reverse
from .models import ErrorLog

class ErrorLoggerAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a sample error log for testing
        self.error_log = ErrorLog.objects.create(
            message='Test Error Message',
            severity='ERROR',
            error_type='SERVER_ERROR'
        )

    def test_error_log_list_view(self):
        # Test accessing the error log list view
        response = self.client.get(reverse('error_log_list'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertContains(response, self.error_log.message)  # Check if the error log is present in the response content

    def test_error_log_detail_view(self):
        # Test accessing the error log detail view
        response = self.client.get(reverse('error_log_detail', kwargs={'pk': self.error_log.pk}))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertContains(response, self.error_log.message)  # Check if the error log message is present in the response content

    # Add more test cases as needed
