# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
