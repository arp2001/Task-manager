from django.urls import path
from .views import task_list, register_view, create_task, edit_task,delete_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('register/', register_view, name='register'),
    path('create/', create_task, name='create_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),


]

