from __future__ import unicode_literals

from django.contrib import admin

from music.models import Album, Artist, Track

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
