# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogApp', '0003_auto_20160226_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='img',
            field=models.ImageField(upload_to=b'images', null=True, verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430', blank=True),
        ),
    ]
