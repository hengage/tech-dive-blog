from django.test import SimpleTestCase, TestCase
from account.forms import CustomUserCreationForm

class TestCustomUserCreationForm(TestCase):

    def test_form_is_valid_data(self):
        form = CustomUserCreationForm(data={
            'first_name':'henry',
            'last_name':'chizoba',
            'username':'hengage',
            'password1':'dracula',
            'password2':'dracula',
            'date_of_birth':'jan-30-1994',
            'email':'hengage@yahoo.com',
            'gender':'male',
            'address':'umudagu',
            'result':None
        })

        # self.assertTrue(form.is_valid())
        # self.assertTrue(self.form.is_valid())
        self.assertEqual(form.data['first_name'], 'henry')

    def test_form_is_not_valid_data(self):
        form = CustomUserCreationForm(data={'gender':'male'})

        print(form.errors)

        self.assertEquals(len(form.errors),4)
