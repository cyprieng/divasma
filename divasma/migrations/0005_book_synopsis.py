# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divasma', '0004_book_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='synopsis',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
