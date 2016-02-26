# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogApp', '0002_auto_20160226_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='img',
            field=models.ImageField(upload_to=b'images', null=True, verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='text',
            field=models.TextField(null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
    ]
