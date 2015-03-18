from django.contrib import admin
from app01.models import BBS,Category,BBS_user
# Register your models here.

admin.site.register(BBS)
admin.site.register(BBS_user)
admin.site.register(Category)