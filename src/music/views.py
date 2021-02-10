from django.shortcuts import render
from rest_framework import permissions, response
from rest_framework_json_api import schemas, views
from rest_framework_swagger import renderers

from .models import Album, Song
from .serializers import AlbumSerializer, SongSerializer


# Create your views here.
class AlbumView(views.ModelViewSet):
    """Albums view."""

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    search_fields = ["title", "year", "genre"]
    filterset_fields = ["title", "year", "genre"]


class SongView(views.ModelViewSet):
    """Songs view."""

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    search_fields = ["title", "singer", "composer", "album__title"]
    filterset_fields = ["title", "singer", "composer", "album__title", "album"]


class SwaggerView(views.RelationshipView):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer]

    def get(self, request):
        generator = schemas.openapi.SchemaGenerator()
        schema = generator.get_schema(request=request)

        return response.Response(schema)
