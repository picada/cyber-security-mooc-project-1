from django.urls import path

from . import views

urlpatterns = [
    path('', views.todos, name='todos'),
    path("add/", views.add, name="add"),
    path("<int:id>/mark-done/", views.mark_done, name="mark_done"),
    path("<int:id>/delete/", views.delete, name="delete"),
]