# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-11 13:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0005_auto_20180211_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='hood_id',
            new_name='hood',
        ),
    ]
