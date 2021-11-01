from django.forms.fields import DateTimeField
from django.test import TestCase
from unittest import mock
import datetime 
from django.db.models import DateTimeField

from account.models import CustomUser



class TestCustomUser(TestCase):

    def setUp(self):
        
        self.user = CustomUser.objects.create(
            username = 'hengage',
            date_of_birth = '1994-10-30',
            date_registered = DateTimeField(auto_now_add=True), 
            gender = 'male',
        )
     
    def test_user_is_created_correctly(self):
        self.assertEquals(self.user.username, 'hengage')
        self.assertEquals(self.user.id, 1)
        self.assertEquals(self.user.gender, 'male')

        print('test_user_is_created_correctly')
   