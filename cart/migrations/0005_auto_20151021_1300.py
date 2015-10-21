# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20151021_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.OneToOneField(null=True, to='cart.Item'),
        ),
    ]
