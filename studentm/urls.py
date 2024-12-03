from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views 
# from rest_framework_simplejwt.views import TokenObtainPairView

# from user.views import 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'), 
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'), 
         
    path('api-auth/', include('rest_framework.urls')), # login and logout views for browsable API
    path('', include('classroom.urls')),
    path('', include('student.urls')),
    path('', include('user.urls')),
    path('', include('teacher.urls')),
]
