from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
import models
#from django.template.context import RequestContext

# Create your views here.

def index(request):
    bbs_list = models.BBS.objects.all()
    user = request.user
    #print 'hello index'
    return render_to_response('index.html',locals())

def bbs_detail(request,bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)
    #print 'hello bbs_details'
    return render_to_response('bbs_detail.html',{'bbs_details':bbs})


def sub_comment(request):
    print request.POST
    bbs_id = request.POST.get('bbs_id')
    return HttpResponseRedirect('/detail/%s'% bbs_id)

def login(request):
    return render_to_response('login.html')

def logout(request):
    auth.logout(request)
    return HttpResponse("<h4>You've just logged out! <a href='/login/'>click here</a> to relogin</h4>")

def account_login(request):
    username = request.POST['user']
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    print user,'====='
    if user is not None: #and user.is_active:
            #correct password and user is marked "active"
            auth.login(request,user)
            return HttpResponseRedirect("/")
    else:
            return render_to_response('login.html',{'err':'Wrong username or password!'})

