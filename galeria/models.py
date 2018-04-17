from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=200, db_index = True)
    slug = models.SlugField(max_length=200, db_index = True, unique = True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'album'
        verbose_name_plural = 'albums'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('galeria:photo_list_by_album', args=[self.slug])


class Photo (models.Model):
    album = models.ForeignKey (Album, related_name = 'photos' )
    name = models.CharField(max_length=200, db_index = True)
    slug = models.SlugField(max_length=200, db_index = True, unique = True)
    image = models.ImageField (upload_to ='photos/%Y/%m/%d')


    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'), )


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('galeria:photo_detail', args = [self.id, self.slug])
