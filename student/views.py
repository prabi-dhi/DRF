from student.models import Student
from student.serializers import StudentSerializer
from rest_framework import generics
from rest_framework import permissions
from student.permissions import IsUserOrReadOnly
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.reverse import reverse

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsUserOrReadOnly]



