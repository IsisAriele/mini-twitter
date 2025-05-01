from django.contrib import admin
from users.models import CustomUser
from django.contrib import admin

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass