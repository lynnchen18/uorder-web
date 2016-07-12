# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meal_id', models.CharField(max_length=200)),
                ('meal_name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('picture', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(max_length=200)),
                ('meals', models.CharField(max_length=200)),
                ('total_price', models.CharField(max_length=200)),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('pickup_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shop_id', models.CharField(max_length=20)),
                ('shop_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=20)),
                ('account', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='shop_id',
            field=models.ForeignKey(to='dataaccess.Shop'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='dataaccess.User'),
        ),
        migrations.AddField(
            model_name='meal',
            name='shop_id',
            field=models.ForeignKey(to='dataaccess.Shop'),
        ),
    ]
