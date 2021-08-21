from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm #, UserChangeForm



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    #form = UserChangeForm
    
    list_display = ['email', 'username', 'first_name', 'last_name', 'date_of_birth', 'is_staff','gender','date_registered' ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'gender')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('first_name', 'last_name', 'email', 'date_of_birth','gender')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


