from django.db import models

class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    class Meta:
        app_label = 'divasma'

    def __str__(self):
        return self.firstname + ' ' + self.lastname
