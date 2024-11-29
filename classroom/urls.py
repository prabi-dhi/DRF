from django.urls import include, path
from rest_framework import routers
# from .views import *

from classroom import views
# router = routers.DefaultRouter()
# router.register(r'classes',ClassroomViewSet)

# urlpatterns = [
#     path('',include(router.urls)),
#     path('api-auth/', include('rest_framework.urls')),
# ]

urlpatterns = [
    path('classroom/', views.ClassroomList.as_view()),
    path('classroom/<int:pk>/', views.ClassroomDetail.as_view()),
]
