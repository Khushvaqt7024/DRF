from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

class UserAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='xushvaqt', password='1234')
        self.token_url = reverse('token_obtain_pair')
        self.list_url = '/api/users/'

    def authenticate(self):
        response = self.client.post(self.token_url, {'username': 'xushvaqt', 'password': '1234'})
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_user_list_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 401)

    def test_user_list_authenticated(self):
        self.authenticate()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_invalid(self):
        self.authenticate()
        data = {"username": "", "email": "notanemail"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, 400)  # Validation error

    def test_create_user_success(self):
        self.authenticate()
        data = {
            "username": "testuser",
            "email": "Khushvaqt.arab@gmail.com",
            "first_name": "Ali",
            "last_name": "Valiyev",
            "age": 25
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['username'], 'testuser')

    def test_update_user(self):
        self.authenticate()
        data = {
            "username": "testuser2",
            "email": "xushvaqt.abdigafforov@gmail.com",
            "first_name": "Ali",
            "last_name": "Valiyev",
            "age": 30
        }
        create = self.client.post(self.list_url, data)
        user_id = create.data['id']
        update_data = {**data, "first_name": "AliUpdated"}
        update = self.client.put(f'{self.list_url}{user_id}/', update_data)
        self.assertEqual(update.status_code, 200)
        self.assertEqual(update.data['first_name'], "AliUpdated")

    def test_delete_user(self):
        self.authenticate()
        data = {
            "username": "todelete",
            "email": "khushvaqt.arab@mail.ru",
            "first_name": "Del",
            "last_name": "User",
            "age": 20
        }
        create = self.client.post(self.list_url, data)
        user_id = create.data['id']
        delete = self.client.delete(f'{self.list_url}{user_id}/')
        self.assertEqual(delete.status_code, 204)
