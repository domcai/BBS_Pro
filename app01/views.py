from django.shortcuts import render_to_response
import models
from django.http import HttpResponseRedirect
#from django.template.context import RequestContext

# Create your views here.

def index(request):
    bbs_list = models.BBS.objects.all()
    #print 'hello index'
    return render_to_response('index.html',{'bbs_list':bbs_list})

def bbs_detail(request,bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)
    #print 'hello bbs_details'
    return render_to_response('bbs_detail.html',{'bbs_details':bbs})


def sub_comment(request):
    print request.POST
    bbs_id = request.POST.get('bbs_id')
    return HttpResponseRedirect('/detail/%s/'% bbs_id)