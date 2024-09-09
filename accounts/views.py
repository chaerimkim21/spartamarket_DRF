from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.core.validators import validate_email
from .validators import validate_signup, validate_update_user
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpView(APIView):
    def post(self, request):
        is_valid, err_msg = validate_signup(request.data)
        if not is_valid:
            return Response({"error": err_msg}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(**request.data)
        serializer = UserSerializer(user)
        res_data = serializer.data
        refresh = RefreshToken.for_user(user)
        res_data['tokens'] = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
        return Response(res_data)


class SignInView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not User.objects.filter(username=username).exists():
            return Response(
                {"error": "존재하지 않는 유저네임입니다." }, status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"error": "유효하지 않은 유저네임이나 비밀번호입니다." }, status=status.HTTP_400_BAD_REQUEST
            )
    
        serializer = UserSerializer(user)
        res_data = serializer.data 

        # token
        refresh = RefreshToken.for_user(user)
        res_data['tokens'] = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
        return Response(res_data)


class SignOutView(APIView):
    pass


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, username):
        user = User.objects.get(username=username)
        is_valid, err_msg = validate_update_user(request.data)

        nickname = request.data.get('nickname')
        user.nickname = nickname
        user.save()
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
