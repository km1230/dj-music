from django.contrib import admin

from .models import Album, Song


# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass
