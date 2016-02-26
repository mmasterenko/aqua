# -*- coding: utf-8 -*-

from django.db import models
from aqualung.utils.storages import MyImgStorage

upload_img = 'images'


def get_img_storage(w=None, h=None, crop=None):
    return MyImgStorage(width=w, height=h, img_path=upload_img, crop=crop)


class Catalog(models.Model):
    class Meta:
        verbose_name_plural = u'каталог'
        verbose_name = u'каталог'

    def __unicode__(self):
        return self.name

    name = models.CharField(u'название каталога', max_length=90, unique=True)


class Goods(models.Model):
    class Meta:
        verbose_name = u'товар'
        verbose_name_plural = u'товары'
        unique_together = ('name', 'catalog')

    def __unicode__(self):
        return self.name

    catalog = models.ForeignKey(Catalog, verbose_name=u'каталог', null=True, blank=True)

    name = models.CharField(u'название', max_length=90)
    price = models.DecimalField(u'цена', max_digits=9, decimal_places=2, null=True, blank=True)
    text = models.TextField(u'описание', null=True, blank=True)
    img = models.ImageField(u'картинка', upload_to=upload_img, null=True, blank=True)


class Attributes(models.Model):
    class Meta:
        verbose_name = u'аттрибут'
        verbose_name_plural = u'аттрибуты'
        unique_together = ('name', 'goods')

    def __unicode__(self):
        return u'%s:%s' % (self.name, self.value)

    goods = models.ForeignKey(Goods, verbose_name=u'товар', null=True, blank=True)

    name = models.CharField(u'имя', max_length=90)
    value = models.CharField(u'значение', max_length=90, null=True, blank=True)
