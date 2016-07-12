# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataaccess', '0002_auto_20151130_0340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='name',
            new_name='shop_name',
        ),
    ]
