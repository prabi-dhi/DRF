from .models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ApiRootView(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('user-list', request=request),
            'students': reverse('student-list', request=request),
            'classroom': reverse('classroom-list', request= request),
        })