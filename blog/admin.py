from django.contrib import admin
from .models import Blog
from parler.admin import TranslatableAdmin
# Register your models here.
admin.site.register(Blog, TranslatableAdmin)
