from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ('date_created', 'completed_at')
