from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "accounts"
urlpatterns = [
    path('', views.SignUpView.as_view(), name="signup"),
    path('login/', views.SignInView.as_view(), name="signin"),
    path('logout/', views.SignOutView.as_view(), name="signout"),
    path('<str:username>/', views.UserProfileView.as_view(), name="profile"),
    path('password/', views.UserPasswordChangeView.as_view(), name="password_change"),
]
