# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-11 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20170811_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='province_name',
            field=models.CharField(blank=True, default='Central', max_length=255, null=True, verbose_name='Province Name'),
        ),
    ]
