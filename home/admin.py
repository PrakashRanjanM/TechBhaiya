from django.contrib import admin
from home.models import Contact,Flames
# Register your models here.

admin.site.register((Contact,Flames))