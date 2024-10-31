from django.contrib import admin
from blog.models import *


class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/test.js',)
        css = {
            'all': ('css/test.css',)
        }
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)