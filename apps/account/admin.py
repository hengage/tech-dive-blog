from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm #, UserChangeForm

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    #form = UserChangeForm

    list_display = [
        'email', 'last_name', 'is_staff',
    ]

    fieldsets= [
        ("Basic User Details", {
            "fields": ['email', 'first_name', 'last_name',]
        }),

        (
            "User Status (sensitive area, proceed with caution)",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ],
                "classes": ["collapse"],
            },
        ),

        (
            'Important Dates',
            {
                "fields": ["date_joined", "last_login"]
            },
        ),

        ("Groups And Permissions", 
            {
                "fields": ["groups", "user_permissions"], 
                "classes": ["collapse"]
            }
        ),
    ]

    add_fieldsets = (
        (
            "User Personal Details",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password",
                ),
            },
        ),

        (
            "User status",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_active"
                ),
            },
        ),
    )
    
    
    
    ordering = ['email']

    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('first_name', 'last_name', 'email',)}),
    # )