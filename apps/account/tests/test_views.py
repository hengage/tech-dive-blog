from django.test import TestCase, Client, SimpleTestCase
from account.models import CustomUser
from django.urls import reverse

class SignupTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')

    def test_SignUp_view_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
