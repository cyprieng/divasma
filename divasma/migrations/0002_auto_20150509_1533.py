# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divasma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='translation_collection',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='translation_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='translation_name',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='translation_place_publisher',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='translation_publisher',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]
