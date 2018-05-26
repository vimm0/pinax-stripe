# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-09 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0007_auto_20170108_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='tax',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='tax_percent',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]
