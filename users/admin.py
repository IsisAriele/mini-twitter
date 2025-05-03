from django.contrib import admin
from users.models import UserModel
from django.contrib import admin

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    pass