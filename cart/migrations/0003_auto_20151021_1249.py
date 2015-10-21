# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20151021_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='delivered_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
