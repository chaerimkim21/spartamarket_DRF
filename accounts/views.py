from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .validators import validate_signup, validate_update_user, validate_delete_user
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class SignUpView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            # POST 요청(회원가입)에는 로그인 상태 불필요
            return [AllowAny()]
        return [IsAuthenticated()] # DELETE 요청에는 (회원 탈퇴) IsAuthenticated() 사용

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
    
    def delete(self, request):
        print(request.user)  # 로그인한 user object
        print(request.data)
        user = request.user

        is_valid, err_msg = validate_delete_user(request.data, user)
        if not is_valid:
            return Response({"error": err_msg}, status=status.HTTP_400_BAD_REQUEST)
        
        user.delete()
        return Response({"message": "회원 탈퇴 성공"}, status=status.HTTP_200_OK)


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
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        is_valid, err_msg = validate_update_user(request.data)
        if not is_valid:
            return Response({"error": err_msg}, status=status.HTTP_400_BAD_REQUEST)
        
        user.username = request.data.get('username', user.username)
        user.nickname = request.data.get('nickname', user.nickname)
        user.email = request.data.get('email', user.email)
        user.birth = request.data.get('birth', user.birth)
        # gender, introduction 입력은 생략 가능
        user.gender = request.data.get('gender', user.gender)
        user.introduction = request.data.get('introduction', user.introduction)
        
        user.save()
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
