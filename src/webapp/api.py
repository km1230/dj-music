"""Default API configuration."""
from typing import List, Tuple

from django.urls import include, path  # type: ignore
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter  # type: ignore
from rest_framework.viewsets import ViewSetMixin  # type: ignore
from rest_framework_swagger.views import get_swagger_view

from music import views as music_views
from users import views as user_views  # type: ignore

# Schema view configuration
# drf_yasg
schema_view = get_schema_view(
    openapi.Info(
        title="Music App API",
        default_version="v1",
        description="Music App API",
        contact=openapi.Contact(email="webmaster@ionata.com.au"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)
# django_rest_swagger
rest_schema_view = get_swagger_view(title="Music App API")


# Add viewsets here. The first argument is the name and the URL regex
routes: List[Tuple[str, ViewSetMixin]] = [
    ("users", user_views.UserView),
    ("sessions", user_views.SessionView),
    ("password-resets", user_views.PasswordResetView),
    ("password-reset-confirmations", user_views.PasswordResetConfirmView),
    ("albums", music_views.AlbumView),
    ("songs", music_views.SongView),
]

v1_router = DefaultRouter()

for regex, viewset in routes:
    v1_router.register(regex, viewset, basename=regex)

# Config api
api = [
    path("", include(v1_router.urls)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("rest_swagger/", rest_schema_view),
]
