# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataaccess', '0005_shop_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='shop_name',
            new_name='name',
        ),
    ]
