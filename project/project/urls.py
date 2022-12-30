from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('notes/', include('notes.urls')),
    path('admin/', admin.site.urls),
]