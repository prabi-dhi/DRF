from django.urls import path, include
from user import views

urlpatterns = [
path('user/', views.UserList.as_view(), name = 'user-list'),
path('user/<int:pk>/', views.UserDetail.as_view(), name = 'user-detail'),  
path('', views.ApiRootView.as_view()),
]
