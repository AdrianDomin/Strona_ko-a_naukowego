from django.contrib import admin
from .models import Album, Photo
# Register your models here.


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields ={'slug': ('name',) }

admin.site.register(Album, AlbumAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields ={ 'name': ('image',), 'slug': ('name',) }

admin.site.register(Photo, PhotoAdmin)
