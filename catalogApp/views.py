# -*- coding: utf-8 -*-

from utils import group_list
from django.shortcuts import render
from django.http import HttpResponse
from .models import Catalog, Goods

general = {
    'keywords': u'водолазное снаряжение',
    'description': u'водолазное снаряжение',
    'title': u'Водолазное оборудование',
    'brandname': u'Моя контора',
    'heading': u'Каталог',
    'subheading': u'',
    'breadcrumbs': [dict(name=u'каталог', url='#')]
}


def categories(req):
    context = {
        'category_rows': group_list(Catalog.objects.all(), 3)
    }
    context.update(general)
    return render(req, 'catalogApp/catalog.html', context=context)


def catalog(req, catalog_id=None):
    context = {'goods': Goods.objects.filter(catalog_id=catalog_id)}
    context.update(general)
    return render(req, 'catalogApp/catalog_item.html', context=context)


def good_item(req, good_id=None):
    context = {'good_item': Goods.objects.get(pk=good_id)}
    context.update(general)
    return render(req, 'catalogApp/good_item.html', context=context)

