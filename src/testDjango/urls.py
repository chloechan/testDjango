from django.conf.urls import patterns, include, url
from testDjango.view import hello, current_datetime,testPostgre,future_datetime

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myfirst.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^testPostgre/$', testPostgre),
    url(r'^time/plus/(\d{1,2})$', future_datetime),
    
)
