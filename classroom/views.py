# from rest_framework import viewsets
# from .serializers import ClassroomSerializer
# from .models import Classroom
# class ClassroomViewSet(viewsets.ModelViewSet):
#     queryset = Classroom.objects.all()
#     serializer_class = ClassroomSerializer
# from rest_framework import viewsets
from .serializers import ClassroomSerializer
from .models import Classroom
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
from django.http import Http404
class ClassroomListApi(APIView):
    def get (self, request):
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many = True)
        return Response(serializer.data)
    
class ClassroomAddApi(APIView):
    def post(self, request):
        # d = request.data
        # d['room_number'] = '11'  
        # d['total_seat'] = '20'  
        serializer = ClassroomSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassroomDetailGetApi(APIView):
    def get(self, request, pk):
        classroom = Classroom.objects.get(pk=pk)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)
    
class ClassroomDetailUpdateApi(APIView):
    def put(self, request, pk, format=None):
        classroom = Classroom.objects.get(pk=pk)
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassroomDetailDeleteApi(APIView):
    def delete(self, request, pk):
        classroom = Classroom.objects.get(pk=pk)
        classroom.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def classroomList(request):
#     if request.method == 'GET':
#         classroom = Classroom.objects.all()
#         serializer = ClassroomSerializer(classroom, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ClassroomSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


