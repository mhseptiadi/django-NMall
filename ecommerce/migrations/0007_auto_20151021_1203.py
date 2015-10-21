# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_auto_20151021_0719'),
    ]

    operations = [
        migrations.CreateModel(
            name='mCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('delivered_date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='mItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(to='ecommerce.mCart')),
                ('product', models.ForeignKey(to='ecommerce.Brand')),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
