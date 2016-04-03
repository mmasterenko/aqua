# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogApp', '0004_catalog_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'&lt;title&gt;', max_length=150, null=True, verbose_name=b'Title', blank=True)),
                ('meta_desc', models.CharField(help_text=b'&lt;meta name="description"&gt;', max_length=250, null=True, verbose_name=b'Description', blank=True)),
                ('meta_keywords', models.CharField(help_text=b'&lt;meta name="keywords"&gt;', max_length=250, null=True, verbose_name=b'Keywords', blank=True)),
                ('brandname', models.CharField(help_text='\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0432\u0441\u0435\u0445 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430\u0445 \u0432 "\u0448\u0430\u043f\u043a\u0435"', max_length=20, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0440\u044d\u043d\u0434\u0430')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
