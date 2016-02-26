# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='catalog',
            field=models.ForeignKey(verbose_name='\u043a\u0430\u0442\u0430\u043b\u043e\u0433', blank=True, to='catalogApp.Catalog', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='attributes',
            unique_together=set([('name', 'goods')]),
        ),
        migrations.AlterUniqueTogether(
            name='goods',
            unique_together=set([('name', 'catalog')]),
        ),
    ]
