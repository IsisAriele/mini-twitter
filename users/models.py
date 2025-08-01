from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    name = models.CharField(max_length=150)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_picture/", blank=True, null=True
    )
    email = models.EmailField(unique=True)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "User Model"
        verbose_name_plural = "Users Models"

    def __str__(self):
        return f"{self.username} - {self.email}"
