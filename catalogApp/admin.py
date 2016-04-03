# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Goods, Attributes, Catalog, GeneralInfo


class GeneralInfoAdmin(admin.ModelAdmin):
    actions = None
    fieldsets = [
        (u'Общая информация', {
            'fields': ('brandname',),
            'classes': ('wide',)
        }),
        (u'для SEO', {
            'fields': ('title', 'meta_keywords', 'meta_desc'),
            'classes': ('collapse', 'wide')
        })
    ]


class AttributesInline(admin.TabularInline):
    model = Attributes
    extra = 0
    can_delete = True


class GoodsAdmin(admin.ModelAdmin):
    inlines = [AttributesInline]
    search_fields = ('name', 'catalog__name')
    list_display = ('name', 'price', 'catalog', 'img')


class AttributesAdmin(admin.ModelAdmin):
    search_fields = ('name', 'value', 'goods__name')
    list_display = ('__unicode__', 'goods')


admin.site.register(Catalog)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Attributes, AttributesAdmin)
admin.site.register(GeneralInfo, GeneralInfoAdmin)

admin.site.site_header = u'Интерфейс администратора'
admin.site.index_title = u'Управление'
