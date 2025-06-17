from django.urls import path

from users.views import UserDetailView, UserMeView

urlpatterns = [
    path("me/", UserMeView.as_view(), name="user_me"),
    path("<str:username>/", UserDetailView.as_view(), name="user_detail"),
]
