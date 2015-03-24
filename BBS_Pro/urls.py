from django.conf.urls import patterns, url, include
from django.contrib import admin
#import app01.urls
#from app01.views import account_login,login,logout
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('app01.urls')),
    (r'^account_login/$','app01.views.account_login'),
    (r'^login/$','app01.views.login'),
    (r'^logout/$','app01.views.logout'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
)