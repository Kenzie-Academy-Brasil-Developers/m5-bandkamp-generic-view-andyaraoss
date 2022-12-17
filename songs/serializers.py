from .models import Song
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    album_id = serializers.SerializerMethodField()

    def get_album_id(self, obj: Song) -> str:
        return obj.album.id

    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]
