from rest_framework import serializers

from .models import Column, Task


class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = ('id', 'title', 'user')
        extra_kwargs = {
            'user': {'write_only': True},
        }


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'column', 'title', 'text', 'date_created', 'date_updated')
        extra_kwargs = {
            'column': {'write_only': True},
        }

