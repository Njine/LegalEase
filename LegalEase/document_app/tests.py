from django.test import TestCase, Client
from django.urls import reverse
from .models import Document

class DocumentAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a sample document for testing
        self.document = Document.objects.create(
            title='Test Document',
            content='Sample content for testing',
            author='Test Author'
        )

    def test_document_list_view(self):
        # Test accessing the document list view
        response = self.client.get(reverse('document_list'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertContains(response, self.document.title)  # Check if the document is present in the response content

    def test_document_detail_view(self):
        # Test accessing the document detail view
        response = self.client.get(reverse('document_detail', kwargs={'pk': self.document.pk}))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertContains(response, self.document.content)  # Check if the document content is present in the response content

    # Add more test cases as needed
