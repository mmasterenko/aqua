# -*- coding: utf-8 -*-

from utils import group_list
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Catalog, Goods, Photos


def get_general(key):
    general = {
        'breadcrumbs': [dict(name=u'Каталог', url=reverse('catalog'))]
    }
    return general.get(key)


def categories(req):
    context = {
        'category_rows': group_list(Catalog.objects.all(), 3)
    }
    return render(req, 'catalogApp/catalog.html', context=context)


def catalog(req, catalog_id=None):
    context = {'goods': Goods.objects.filter(catalog_id=catalog_id)}
    catalog_name = Catalog.objects.get(pk=catalog_id).name
    local_general = {
        'title': catalog_name,
        'heading': catalog_name,
        'breadcrumbs': get_general('breadcrumbs') + [dict(name=catalog_name, url=reverse('catalog_item', args=[catalog_id]))]
    }
    context.update(local_general)
    return render(req, 'catalogApp/catalog_item.html', context=context)


def good_item(req, good_id=None):
    good = Goods.objects.get(pk=good_id)
    images = Photos.objects.filter(goods_id=good_id)
    context = {'good_item': good, 'images': images}
    local_general = {
        'title': good.name,
        'breadcrumbs': get_general('breadcrumbs') + [
            dict(name=good.catalog.name, url=reverse('catalog_item', args=[good.catalog_id])),
            dict(name=good.name, url=reverse('good_item', args=[good.id]))]
    }
    context.update(local_general)
    return render(req, 'catalogApp/good_item.html', context=context)

