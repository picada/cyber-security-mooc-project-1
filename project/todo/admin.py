from django.contrib import admin

from .models import ToDo
from .models import User

admin.site.register(ToDo)
admin.site.register(User)