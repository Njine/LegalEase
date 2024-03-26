from django.test import TestCase, Client
from django.urls import reverse
from .models import PermissionLevel, SecurityGroup

class SecurityAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create sample permission levels
        self.permission1 = PermissionLevel.objects.create(name='Permission 1')
        self.permission2 = PermissionLevel.objects.create(name='Permission 2')
        # Create a sample security group with permissions
        self.security_group = SecurityGroup.objects.create(name='Test Group')
        self.security_group.permissions.add(self.permission1, self.permission2)

    def test_security_group_list_view(self):
        # Test accessing the security group list view
        response = self.client.get(reverse('security_group_list'))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertContains(response, self.security_group.name)  # Check if the security group name is present in the response content

    def test_security_group_detail_view(self):
        # Test accessing the security group detail view
        response = self.client.get(reverse('security_group_detail', kwargs={'pk': self.security_group.pk}))
        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertContains(response, self.security_group.name)  # Check if the security group name is present in the response content

    # Add more test cases as needed
