from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=False)
    date_registered = models.DateTimeField(auto_now_add=True)
    
    # Choices for gender select.
    GENDER_SELECT = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Binary', 'Binary'),
        ('Non-Binary', 'Non-Binary'),
        ('Genderfluid', 'Genderfluid'),
        ('Agender', 'Agender'),
        ('Bigender', 'Bigender'),
        ('Polygender', 'Polygender'),
        ('Neutrois', 'Neutrois'),
        ('Gender Apathetic', 'Gender Apathetic'),
        ('Intergender', 'Intergender'),
    )

    gender = models.CharField(max_length=19, choices=GENDER_SELECT, default='Male')
    result = models.FileField(blank=True)
    #id_photo = models.ImageField()