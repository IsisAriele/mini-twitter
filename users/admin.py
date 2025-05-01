from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('name', 'bio', 'profile_picture',),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)