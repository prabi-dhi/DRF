from django.urls import path, include
from student import views

urlpatterns = [
    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>', views.StudentDetail.as_view()),
]
