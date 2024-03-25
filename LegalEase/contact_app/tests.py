from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserCreationForm, CustomPasswordChangeForm

class AuthenticationManagerTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_login_view(self):
        # Test login view with valid credentials
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)  # Redirects to profile page upon successful login

        # Test login view with invalid credentials
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Returns login page upon failed login

    def test_registration_view(self):
        # Test registration view with valid data
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'newpassword123', 'password2': 'newpassword123'})
        self.assertEqual(response.status_code, 302)  # Redirects to profile page upon successful registration

        # Test registration view with invalid data
        response = self.client.post(reverse('register'), {'username': '', 'password1': 'newpassword123', 'password2': 'newpassword123'})
        self.assertEqual(response.status_code, 200)  # Returns registration page upon failed registration

    def test_profile_view(self):
        # Test profile view for authenticated user
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)  # Returns profile page for authenticated user

        # Test profile view for unauthenticated user
        self.client.logout()
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Redirects to login page for unauthenticated user

    # Add more test cases for password change view, user management view, etc.

    # Cleanup after tests
    def tearDown(self):
        self.user.delete()
