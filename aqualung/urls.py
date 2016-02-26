from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'aqualung.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^aquadmin/', include(admin.site.urls)),
]
