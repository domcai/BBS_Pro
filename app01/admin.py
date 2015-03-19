from django.contrib import admin
from app01.models import BBS,Category,BBS_user
# Register your models here.

class BBS_Admin(admin.ModelAdmin):
    list_display = ('title','summary','author','view_count','create_at',)
    list_filter = ('create_at',)
    search_fields = ('title','author__user__username',)
admin.site.register(BBS,BBS_Admin)
admin.site.register(BBS_user)
admin.site.register(Category)