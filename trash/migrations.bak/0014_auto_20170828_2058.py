# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 15:58
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('AutoGrade', '0013_auto_20170828_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assignment_files',
            field=filer.fields.file.FilerFileField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filer_assignment_files', to='filer.File'),
        ),
    ]