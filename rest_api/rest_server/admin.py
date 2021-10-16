from django.contrib import admin

# Register your models here.
from .models import Sports, Article
admin.site.register(Sports)
admin.site.register(Article)