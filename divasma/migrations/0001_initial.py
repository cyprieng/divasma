# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('original_title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('publisher', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('place_published', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('isbn', models.CharField(max_length=16)),
                ('image', models.URLField()),
                ('series', models.CharField(max_length=100)),
                ('translation_name', models.CharField(max_length=255)),
                ('translation_publisher', models.CharField(max_length=100)),
                ('translation_place_publisher', models.CharField(max_length=100)),
                ('translation_collection', models.CharField(max_length=255)),
                ('translation_date', models.DateField()),
                ('author', models.ForeignKey(to='divasma.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='divasma.Genre'),
        ),
    ]
