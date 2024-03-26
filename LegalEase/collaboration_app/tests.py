from django.test import TestCase, Client
from django.urls import reverse
from .models import Team
from django.contrib.auth.models import User

class CollaborationAppTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username='test_user', email='test@example.com', password='password')

    def test_team_creation(self):
        # Test creation of a team
        team_count_before = Team.objects.count()
        new_team_data = {
            'name': 'New Team',
            'members': [self.user.id]  # Assuming the test user is a member of the team
        }
        response = self.client.post(reverse('create_team'), new_team_data)
        self.assertEqual(response.status_code, 302)  # Redirects to team list page upon successful creation
        self.assertEqual(Team.objects.count(), team_count_before + 1)  # Team count increases by 1

    # Add more test cases for team listing, updating, deleting, etc.

    # Cleanup after tests
    def tearDown(self):
        self.user.delete()
