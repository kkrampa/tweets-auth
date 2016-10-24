from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TestUserApi(APITestCase):

    def test_create(self):
        response = self.client.post('/users/register/', {
            'username': 'test',
            'password': 'dummy',
            'repeat_password': 'dummy',
            'email': 'dummy@example.com',
            'first_name': 'Test',
            'last_name': 'Test'
        })
        self.assertEqual(response.status_code, 201)
        self.assertDictEqual(
            response.json(),
            {'email': 'dummy@example.com', 'last_name': 'Test', 'first_name': 'Test', 'username': 'test'}
        )
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_without_username(self):
        response = self.client.post('/users/register/', {
            'password': 'dummy',
            'repeat_password': 'dummy',
            'email': 'dummy@example.com',
            'first_name': 'Test',
            'last_name': 'Test'
        })
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.json(), {'username': ['This field is required.']})

    def test_available_username(self):
        response = self.client.get('/users/check_username_availability/', {'username': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {'available': True})

    def test_not_available_username(self):
        User.objects.create_user('test', 'test@example.com', 'dummy')

        response = self.client.get('/users/check_username_availability/', {'username': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {'available': False})
