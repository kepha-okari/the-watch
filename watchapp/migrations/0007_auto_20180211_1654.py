# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-11 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0006_auto_20180211_1653'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='hood_id',
            new_name='estate',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='hood',
            new_name='estate',
        ),
    ]
