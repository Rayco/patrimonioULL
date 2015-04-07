# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models, migrations


def add_basic_staff_permission(apps, schema_editor):
    ContentType = apps.get_model('contenttypes.ContentType')
    Permission = apps.get_model('auth.Permission')
    content_type = ContentType.objects.get(app_label='auth', model='user')
    Permission.objects.create(
        content_type=content_type,
        codename='basic_staff',
        name='Can access Basic Admin Site')


def delete_basic_staff_permission(apps, schema_editor):
    apps.get_model('auth.Permission').objects.get(
        codename='basic_staff').delete()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(
            add_basic_staff_permission,
            delete_basic_staff_permission),
    ]
