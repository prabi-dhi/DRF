from django.contrib import admin
from django.urls import path, include
# from user.views import 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('classroom.urls')),
    path('', include('student.urls')),
    path('', include('user.urls')),
    path('', include('teacher.urls')),
]
