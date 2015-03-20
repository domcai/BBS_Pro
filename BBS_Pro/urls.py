from django.conf.urls import patterns, url, include
from django.contrib import admin
#import app01.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('app01.urls')),
)