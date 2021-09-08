from django.contrib import admin

from foxstraat.core.music.models import Song


class SongAdmin(admin.ModelAdmin):
    search_fields = ("object_id",)


admin.site.register(Song, SongAdmin)