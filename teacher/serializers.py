from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    # user= serializers.ReadOnlyField(source = 'user.username')

    class Meta:
        model = Teacher
        fields = ['id', 'name','user']
