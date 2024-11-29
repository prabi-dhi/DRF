from django.urls import path, include
from user import views

urlpatterns = [
path('user/', views.UserList.as_view()),
path('user/<int:pk>/', views.UserDetail.as_view()),  
]
