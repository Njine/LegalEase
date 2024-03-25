from django.test import TestCase, Client
from django.urls import reverse
from .models import Event

class CalendarAppTestCase(TestCase):
    def setUp(self):
        # Create a test event
        self.event = Event.objects.create(title='Test Event', description='This is a test event')

    def test_event_creation(self):
        # Test creation of an event
        event_count_before = Event.objects.count()
        new_event_data = {
            'title': 'New Event',
            'description': 'This is a new event'
        }
        response = self.client.post(reverse('create_event'), new_event_data)
        self.assertEqual(response.status_code, 302)  # Redirects to event detail page upon successful creation
        self.assertEqual(Event.objects.count(), event_count_before + 1)  # Event count increases by 1

    # Add more test cases for event listing, updating, deleting, etc.

    # Cleanup after tests
    def tearDown(self):
        self.event.delete()
