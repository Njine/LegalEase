from django.test import TestCase
from django.urls import reverse
from .models import Case

class CaseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Case.objects.create(case_number='12345', title='Test Case', description='Test Description')

    def test_case_title(self):
        case = Case.objects.get(id=1)
        expected_object_name = f'{case.title}'
        self.assertEquals(expected_object_name, 'Test Case')

    def test_case_case_number(self):
        case = Case.objects.get(id=1)
        expected_object_name = f'{case.case_number}'
        self.assertEquals(expected_object_name, '12345')

class CaseListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 cases for pagination tests
        number_of_cases = 13
        for case_num in range(number_of_cases):
            Case.objects.create(case_number=f'Case {case_num}', title=f'Test Case {case_num}', description=f'Test Description {case_num}')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/cases/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('case-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('case-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'case_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('case-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['case_list']) == 10)

    def test_lists_all_cases(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('case-list')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['case_list']) == 3)
