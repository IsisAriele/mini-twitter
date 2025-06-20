"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from authentication.urls import urlpatterns as auth_urls
from users.urls import urlpatterns as user_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Mini Twitter API",
        default_version="v1",
        description="Documentação da API de rede social com Django REST",
        terms_of_service="https://www.seusite.com/termos/",
        contact=openapi.Contact(email="seuemail@exemplo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(
        permissions.AllowAny if settings.DEBUG else permissions.IsAdminUser,
    ),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include(auth_urls)),
    path("users/", include(user_urls)),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
