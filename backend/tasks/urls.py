from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.get_tasks),
    path('tasks/create', views.create_task),
    path('tasks/<int:id>', views.update_task),
    path('tasks/delete/<int:id>', views.delete_task),
]