from users.views import UserMeView, UserDetailView

from django.urls import path

urlpatterns = [
    path("me/", UserMeView.as_view(), name="user_me"),
    path("<str:username>/", UserDetailView.as_view(), name="user_detail"),
]
