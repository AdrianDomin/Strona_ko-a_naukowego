from django.shortcuts import render, get_object_or_404
from .models import Album, Photo


# Create your views here.


def photo_list(request, album_slug=None):
    album = None
    albums = Album.objects.all()
    photos = Photo.objects.all()

    if album_slug:
        album = get_object_or_404(Album, slug = album_slug)
        photos = photos.filter(album=album)

    return render(request, 'galeria/photo/list.html', {'album':album, "albums":albums, 'photos':photos})



def photo_detail (request, id, slug):
    photo = get_object_or_404(Photo, id=id, slug=slug)

    return render(request, 'galeria/photo/detail.html', {'photo': photo})
