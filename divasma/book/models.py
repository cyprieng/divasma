from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    author = models.ForeignKey('divasma.author.Author')
    slug = models.SlugField()

    publisher = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    place_published = models.CharField(max_length=100)
    date = models.DateField()
    isbn = models.CharField(max_length=16)
    image = models.URLField()
    genre = models.ManyToManyField('Genre', through='BookGenre')
    series = models.CharField(max_length=100)

    translation_name = models.CharField(max_length=255)
    translation_publisher = models.CharField(max_length=100)
    translation_place_publisher = models.CharField(max_length=100)
    translation_collection = models.CharField(max_length=255)
    translation_date = models.DateField()

    class Meta:
        app_label = 'divasma'

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.s = slugify(self.title + self.author.lastname)

        super(Book, self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=100)

class BookGenre(models.Model):
    book = models.ForeignKey('Book')
    genre = models.ForeignKey('Genre')

    class Meta:
        app_label = 'divasma'
