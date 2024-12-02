from rest_framework import serializers
from .models import User
from student.models import Student

class UserSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedRelatedField(queryset=Student.objects.all(),many = True, view_name= 'student-detail', required = False)

    class Meta:
        model = User
        fields = ['url','id', 'username', 'students']