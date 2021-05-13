from django.contrib import admin

# Register your models here.

from. models import Blog
from. models import Team
admin.site.register(Blog)
admin.site.register(Team)