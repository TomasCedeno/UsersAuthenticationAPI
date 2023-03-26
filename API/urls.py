from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from usersAPI import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailUpdateDeleteView.as_view()),
    path('user/add/rol/<int:pk>/', views.AddRolToUserView.as_view()),
    path('user/remove/rol/<int:pk>/', views.RemoveRolFromUserView.as_view()),
    path('rol/', views.ListCreateRolView.as_view()),
    path('rol/<int:pk>', views.DeleteRolView.as_view()),
    path('rol/add/permission/<int:pk>/', views.AddPermissionToRolView.as_view()),
    path('rol/remove/permission/<int:pk>/', views.RemovePermissionFromRolView.as_view()),
    path('permission/', views.ListCreatePermissionView.as_view()),
    path('permission/<int:pk>', views.DeletePermissionView.as_view()),
]