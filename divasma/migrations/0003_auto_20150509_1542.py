# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divasma', '0002_auto_20150509_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='original_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
