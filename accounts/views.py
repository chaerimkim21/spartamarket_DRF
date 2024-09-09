from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.core.validators import validate_email
from .validators import validate_signup

class SignUpView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        nickname = request.data.get('nickname')
        birth = request.data.get('birth')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')

        is_valid, err_msg = validate_signup(request.data)
        if not is_valid:
            return Response({"error": err_msg}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            password=password,
            nickname=nickname,
            birth=birth,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        print(user)

        return Response({})
    

class SignInView(APIView):
    pass

class SignOutView(APIView):
    pass

class UserProfileView(APIView):
    pass
    # permission_classes = [IsAuthenticated]

    # def get(self, request, username):
    #     user = User.objects.get(username=username)
    #     serializer = UserSerialzier(user)
    #     return Response(serializer.data)
    
    # def put(self, request, username):
    #     user = User.objects.get(username=username)
    #     nickname = request.data.get('nickname')
    #     print(nickname)

    #     return Response()