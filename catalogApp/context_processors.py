# -*- coding: utf-8 -*-

from .models import GeneralInfo


def general_info(req):
    info = GeneralInfo.objects.first()
    general = {
        'keywords': info.meta_keywords,
        'description': info.meta_desc,
        'title': info.title,
        'brandname': info.brandname,
        'heading': u'Каталог',
        'subheading': u'',
    }
    result = {'general_info': info}
    result.update(general)
    return result

