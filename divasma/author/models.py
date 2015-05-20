from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'divasma'

    def __str__(self):
        return self.name
