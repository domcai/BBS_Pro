from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BBS(models.Model):
    title = models.CharField(max_length=64)
    category = models.ForeignKey('Category')
    summary = models.CharField(max_length=256,blank=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    administrator = models.ForeignKey('BBS_user')
    
    def __unicode__(self):
        return self.name
    
class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128,default='This guy is too lazy to leave anything!')
    photo = models.ImageField(upload_to='upload_imgs/',default='upload_imgs/user-1.jpg')
    
    def __unicode__(self):
        return self.user.username