from django.conf.urls import include, url
from django.contrib import admin
from .utils import extra_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'aqualung.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # on production server it's better to use nginx for serve static
    url(r'^media/(?P<path>images/.+(?:\.jpeg|\.jpg|\.png))$', extra_views.media, name='media'),
    url(r'^media/(?P<path>files/.+(?:\.pdf|\.doc|\.docx|\.txt))$', extra_views.media, name='media'),

    url(r'^aquadmin/', include(admin.site.urls)),
]
