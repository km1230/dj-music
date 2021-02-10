from rest_framework_json_api import serializers

from .models import Album, Song


class SongSerializer(serializers.ModelSerializer):
    """Song serializer."""

    class Meta:
        """Meta of song serializer."""

        model = Song
        fields = ["title", "singer", "composer", "album"]

class AlbumSerializer(serializers.ModelSerializer):
    """Album serializer."""

    class Meta:
        """Meta of album serializer."""

        model = Album
        fields = ["title", "year", "genre"]    

    included_serializers = {"songs": SongSerializer}
