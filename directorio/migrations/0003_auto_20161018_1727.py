# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-18 22:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0002_auto_20161018_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='directorio',
            old_name='user',
            new_name='usuario',
        ),
    ]