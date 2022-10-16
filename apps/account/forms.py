from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    # password is a "custom" field on the UserCreationForm, since it does not exist as a model field on the User model. 
    # Meta.widgets will not work for this custom field, so I redefined it's field and widget here.
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class':'form-control',})
    )
    password1 = None
    password2 = None
            
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }

        help_texts = {
            'first_name': 'Your first name',
        }

    field_order = [
        'first_name',  'last_name', 'email',  'password',
    ]
        
