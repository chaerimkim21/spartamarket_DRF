from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


app_name = "accounts"
urlpatterns = [
    path('', views.SignUpView.as_view(), name="signup"),
    path('login/', views.SignInView.as_view(), name="signin"),
    path('<str:username>/', views.UserProfileView.as_view(), name="profile"),
]
