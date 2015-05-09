# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divasma', '0003_auto_20150509_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='collection',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
