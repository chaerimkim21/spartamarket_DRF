from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


app_name = "accounts"
urlpatterns = [
    path("", views.SignUpView.as_view(), name="signup"),
    path('login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('<str:username>/', views.UserProfileView.as_view(), name="profile"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

]
