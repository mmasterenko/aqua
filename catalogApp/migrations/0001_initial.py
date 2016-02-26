# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=90, verbose_name='\u0438\u043c\u044f')),
                ('value', models.CharField(max_length=90, null=True, verbose_name='\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u0430\u0442\u0442\u0440\u0438\u0431\u0443\u0442',
                'verbose_name_plural': '\u0430\u0442\u0442\u0440\u0438\u0431\u0443\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=90, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430')),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0442\u0430\u043b\u043e\u0433',
                'verbose_name_plural': '\u043a\u0430\u0442\u0430\u043b\u043e\u0433',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=90, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('price', models.DecimalField(null=True, verbose_name='\u0446\u0435\u043d\u0430', max_digits=9, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name': '\u0442\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0442\u043e\u0432\u0430\u0440\u044b',
            },
        ),
        migrations.AddField(
            model_name='attributes',
            name='goods',
            field=models.ForeignKey(verbose_name='\u0442\u043e\u0432\u0430\u0440', blank=True, to='catalogApp.Goods', null=True),
        ),
    ]
