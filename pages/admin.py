from django.contrib import admin
from .models import Works, Home
from parler.admin import TranslatableAdmin

# Register your models here.
admin.site.register(Works, TranslatableAdmin)
admin.site.register(Home)