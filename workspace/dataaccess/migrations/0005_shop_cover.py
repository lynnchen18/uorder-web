# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dataaccess', '0004_auto_20151201_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='cover',
            field=models.CharField(default=datetime.datetime(2015, 12, 13, 8, 24, 1, 487433, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
