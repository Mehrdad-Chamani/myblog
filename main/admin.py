from django.contrib import admin
from django.contrib.auth.models import Group

from .models import BlogPost, BlogTag, Comment


# Register your models here.

# register models
admin.site.register(BlogPost)
admin.site.register(BlogTag)
admin.site.register(Comment)

# unregister models
admin.site.unregister(Group)


