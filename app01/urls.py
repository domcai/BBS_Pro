from django.conf.urls import patterns, url
#from views import bbs_detail,index
from app01 import views

urlpatterns = patterns('',
    url(r'^detail/(\d+)/$', views.bbs_detail),
    url(r'^sub_comment/$', views.sub_comment),
    url(r'^$',views.index),
)