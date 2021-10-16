from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Sport events API",
      default_version='v1',
      description="Project description",
      terms_of_service="Public service",
      contact=openapi.Contact(email="no@email.provided"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('doc(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0)),
   path('doc/', schema_view.with_ui('swagger', cache_timeout=0))
]
