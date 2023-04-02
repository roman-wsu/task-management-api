from django.urls import path

from .views import ColumnListCreateView, ColumnRetrieveUpdateDestroyAPIView, TaskListCreateView, \
    TaskRetrieveUpdateDestroyAPIView

app_name = 'tasks'
urlpatterns = [
    path('column/',
        ColumnListCreateView.as_view(),
         name='column-list'),
    path('column/<uuid:column_id>/',
        ColumnRetrieveUpdateDestroyAPIView.as_view(),
         name='column-detail'),
    path('column/<uuid:column_id>/task/',
        TaskListCreateView.as_view(),
         name='task-list'),
    path('column/<uuid:id>/task/<uuid:task_id>/',
        TaskRetrieveUpdateDestroyAPIView.as_view(),
         name='task-detail'),
]
