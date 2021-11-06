from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    # password1 and password2 are "custom" fields on the UserCreationForm since they do not exist as model fields on the User model. Meta.widgets will not work for these custom fields, so I redefined their fields and their widgets here.
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class':'form-control',})
    )

    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(attrs={'class':'form-control',})
    )
            

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }

        help_texts = {
            'username': None,
        }

    field_order = [
        'first_name',  'last_name', 
        'username','email',   
        'password1', 'password2',
    ]
        
