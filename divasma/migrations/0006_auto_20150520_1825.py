# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divasma', '0005_book_synopsis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='lastname',
        ),
    ]
