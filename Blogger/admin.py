from django.contrib import admin
from Blogger.models import Post,BloggerComment
# Register your models here.

admin.site.register((Post,BloggerComment))