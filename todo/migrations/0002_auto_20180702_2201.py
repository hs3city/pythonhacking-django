# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-02 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('To do', 'Aktywny'), ('Done!', 'Wykonane')], max_length=10),
        ),
    ]