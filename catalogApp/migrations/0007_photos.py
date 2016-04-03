# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogApp', '0006_auto_20160403_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'images', null=True, verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430', blank=True)),
                ('goods', models.ForeignKey(verbose_name='\u0442\u043e\u0432\u0430\u0440', blank=True, to='catalogApp.Goods', null=True)),
            ],
            options={
                'verbose_name': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f',
            },
        ),
    ]
