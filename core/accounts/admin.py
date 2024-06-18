from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    model = User  # Model associated with this admin class.
    list_display = ['email', 'is_superuser', 'is_active']  # Columns to display in the admin list view.
    list_filter = ['email', 'is_superuser', 'is_active']  # Filters for the list view.
    search_fields = ['email', ]  # Fields to include in the search.
    ordering = ['email', ]  # Default ordering of the list view.
    
    fieldsets = [  # Fields to display on the change form.
        ["Authentication", {'fields': ('email', 'password')}],
        ["Permissions", {'fields': ("is_staff", "is_active", "is_superuser")}],
        ["Group Permissions", {'fields': ("groups", "user_permissions")}],
        ["Important Dates", {'fields': ("last_login", )}]
    ]
    
    add_fieldsets = [  # Fields to display on the add form.
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')
        })
    ]

admin.site.register(User, CustomUserAdmin)  # Register the User model with the custom admin.
admin.site.register(Profile)  # Register the Profile model.
