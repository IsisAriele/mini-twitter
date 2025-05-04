from users.views import UserMeView

from django.urls import path

urlpatterns = [
    path("me/", UserMeView.as_view(), name="user_me"),
]