from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm #, UserChangeForm



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    #form = UserChangeForm
    
    list_display = ['email', 'username', 'first_name', 'last_name',  'is_staff','date_registered' ]

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('first_name', 'last_name', 'email',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


