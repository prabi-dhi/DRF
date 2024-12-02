from django.urls import include, path
from . import views

urlpatterns = [
    path('classroom/', views.ClassroomListApi.as_view(), name ='classroom-list'),
    path('classroom/add', views.ClassroomAddApi.as_view()),
    path('classroom/<int:pk>/', views.ClassroomDetailGetApi.as_view()),
    path('classroom/update/<int:pk>/', views.ClassroomDetailUpdateApi.as_view()),
    path('classroom/delete/<int:pk>/', views.ClassroomDetailDeleteApi.as_view()),
]
