from django.conf.urls import patterns, url
#from views import bbs_detail,index
from app01 import views

urlpatterns = patterns('',
    url(r'^detail/(\d+)/$', views.bbs_detail),
    url(r'^category/(\d+)/$', views.category),
    url(r'^sub_comment/$', views.sub_comment),
    url(r'^bbs_pub/$', views.bbs_pub),
    url(r'^bbs_sub/$', views.bbs_sub),
    url(r'^$',views.index),
)