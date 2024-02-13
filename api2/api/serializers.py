from rest_framework import serializers
from .models import Task, Role


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model=Task
        fields='__all__'
        read_only_fields=['created_at','username','updated_at','updated_by']