from django.test import SimpleTestCase, TestCase
from account.forms import CustomUserCreationForm

class TestCustomUserCreationForm(TestCase):

    def test_form_data_is_valid(self):
        form = CustomUserCreationForm(data={
            'username':'hengage',
            'password1':'123456789$',
            'password2':'123456789$',
        })

        print(form.data)
        if form.errors:
            print(form.errors)
        else:
            print('No errors')

        self.assertTrue(form.is_valid())
        self.assertEqual(form.data['username'], 'hengage')

    def test_form_data_is_not_valid(self):
        form = CustomUserCreationForm(data={})

        print(form.errors)

        self.assertEquals(len(form.errors), 3)
        self.assertFalse(form.is_valid())
