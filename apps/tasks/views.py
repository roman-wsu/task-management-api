from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Column, Task
from .serializers import ColumnSerializer, TaskSerializer


class ColumnListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ColumnSerializer

    def get_queryset(self):
        return Column.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        data['user'] = request.user.id
        print(data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ColumnRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ColumnSerializer
    lookup_field = 'column_id'

    def get_object(self):
        try:
            return Column.objects.get(id=self.request.parser_context['kwargs'].get('column_id', None))
        except Column.DoesNotExist:
            raise Http404


class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(column=self.request.parser_context['kwargs'].get('column_id', None))

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        try:
            column = Column.objects.get(id=self.request.parser_context['kwargs'].get('column_id', None))
            data['column'] = column.id
        except Column.DoesNotExist:
            raise Http404

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ColumnSerializer
    lookup_field = 'id'

    def get_object(self):
        try:
            return Column.objects.get(id=self.request.parser_context['kwargs'].get('id', None))
        except Column.DoesNotExist:
            raise Http404
