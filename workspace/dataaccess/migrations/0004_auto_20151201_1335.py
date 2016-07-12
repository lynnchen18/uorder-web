# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataaccess', '0003_auto_20151130_0345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='meal_name',
            new_name='cover',
        ),
        migrations.RenameField(
            model_name='meal',
            old_name='picture',
            new_name='name',
        ),
    ]
