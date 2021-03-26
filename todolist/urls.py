from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_todo/', views.add_todo),
    path('delete_task/<int:task_id>', views.delete_task),
    path('update_task/<int:task_id>', views.update_task),
    path('fetch_tasks/', views.fetch_tasks),
]
