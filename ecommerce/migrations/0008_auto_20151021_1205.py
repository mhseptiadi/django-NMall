# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_auto_20151021_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='mitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='mitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='mCart',
        ),
        migrations.DeleteModel(
            name='mItem',
        ),
    ]
