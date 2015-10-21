# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20151021_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='cart.Item', null=True),
        ),
    ]
