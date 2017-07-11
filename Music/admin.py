from django.contrib import admin

# Register your models here.
from Music.models import Album,Song

admin.site.register(Album)
admin.site.register(Song)