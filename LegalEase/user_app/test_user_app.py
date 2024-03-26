from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import CustomUser

class UserAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.client.login(username='test_user', password='test_password')
        self.user_profile = UserProfile.objects.create(user=self.user, full_name='Test User', email='test@example.com')

    def test_user_profile_list_view(self):
        # Test accessing the user profile list view
        response = self.client.get(reverse('user_profile_list'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertContains(response, self.user_profile.full_name)  # Check if the user profile full name is present in the response content

    def test_user_profile_detail_view(self):
        # Test accessing the user profile detail view
        response = self.client.get(reverse('user_profile_detail', kwargs={'pk': self.user_profile.pk}))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertContains(response, self.user_profile.full_name)  # Check if the user profile full name is present in the response content

    # Add more test cases as needed
