# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-27 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entitlements', '0014_auto_20200115_2022'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='courseentitlement',
            unique_together=set([('course_uuid', 'order_number')]),
        ),
    ]
