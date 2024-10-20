from django.urls import path
from do.views import TasksView,AddTask

urlpatterns = [
    path('',TasksView.as_view(),name='tasks'),
    path('add/',AddTask.as_view(),name='add'),
]