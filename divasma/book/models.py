from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey('Author')
    slug = models.SlugField()
    publisher = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    place_published = models.CharField(max_length=100)
    collection = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    isbn = models.CharField(max_length=16)
    image = models.URLField()
    genre = models.ManyToManyField('Genre')
    series = models.CharField(max_length=100, null=True, blank=True)
    translation_name = models.CharField(max_length=255, null=True, blank=True)
    translation_publisher = models.CharField(max_length=100, null=True, blank=True)
    translation_place_publisher = models.CharField(max_length=100, null=True, blank=True)
    translation_collection = models.CharField(max_length=255, null=True, blank=True)
    translation_date = models.DateField(null=True, blank=True)
    synopsis = models.TextField()

    class Meta:
        app_label = 'divasma'

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title + '-' + str(self.author))

        super(Book, self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'divasma'
