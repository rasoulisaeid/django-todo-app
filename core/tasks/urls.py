from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, home

app_name = 'tasks'

urlpatterns = [
    path("home", home, name='home'),
    path('tasks/', TaskListView.as_view(), name='list'),
    path('tasks/create/', TaskCreateView.as_view(), name='create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
]