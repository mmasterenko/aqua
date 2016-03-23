# -*- coding: utf-8 -*-

from utils import group_list
from django.shortcuts import render
from .models import Catalog


def categories(req):
    general = {
        'keywords': u'водолазное снаряжение',
        'description': u'водолазное снаряжение',
        'title': 'Aqua',
        'heading': u'Каталог',
        'subheading': u'',
        'breadcrumbs': [dict(name=u'каталог', url='#')]
    }
    context = {
        'category_rows': group_list(Catalog.objects.all(), 3)
    }
    context.update(general)
    return render(req, 'catalogApp/catalog.html', context=context)
