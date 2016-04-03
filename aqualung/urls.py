from django.conf.urls import include, url
from django.contrib import admin
from utils import extra_views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'catalogApp.views.categories', name='home'),
    url(r'^catalog$', 'catalogApp.views.categories', name='catalog'),
    url(r'^catalog/(?P<catalog_id>[0-9]+)', 'catalogApp.views.catalog', name='catalog_item'),
    url(r'^goods/(?P<good_id>[0-9]+)', 'catalogApp.views.good_item', name='good_item'),

    # on production server it's better to use nginx for serve static
    url(r'^media/(?P<path>images/.+(?:\.jpeg|\.jpg|\.png))$', extra_views.media, name='media'),
    url(r'^media/(?P<path>files/.+(?:\.pdf|\.doc|\.docx|\.txt))$', extra_views.media, name='media'),

    url(r'^aquadmin/', include(admin.site.urls)),
]
