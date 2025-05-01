from authentication.views import CreateCustomUserView

from django.urls import path

urlpatterns = [
    path("register/", CreateCustomUserView.as_view(), name="create_custom_user"),
]