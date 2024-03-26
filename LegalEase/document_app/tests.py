from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Document

class DocumentAppTestCase(TestCase):
    def setUp(self):
        # Create a User instance
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        self.document = Document.objects.create(
            title='Test Document',
            content='Test Content',
            author=self.user,  # Assign the User instance to the author field
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
