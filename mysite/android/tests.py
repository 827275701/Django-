from django.test import TestCase, Client


# Create your tests here.

class SimpleTest(TestCase):
    def test_login(self):
        c = Client(HTTP_USER_AGENT='Mozilla/5.0')
        response = c.post('/android/login/',
                          {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)
