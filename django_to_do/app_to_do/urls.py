from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task', views.add_task, name='add_task'),
    path('add_task_record', views.add_task_record, name='add_task_record'),
]