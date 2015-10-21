# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(default=b'', max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=0, max_digits=19, decimal_places=10),
        ),
    ]
