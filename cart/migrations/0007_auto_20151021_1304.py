# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20151021_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='cart',
            field=models.ForeignKey(default=0, to='cart.Cart'),
        ),
    ]
