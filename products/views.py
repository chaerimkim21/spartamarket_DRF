from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Product
from .validators import validate_product_upload, validate_product_update, validate_product_delete
from django.core.exceptions import PermissionDenied
from .serializers import ProductSerializer, ProductDetailSerializer
import json


class ProductListView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            # GET 요청에는 로그인 상태 불필요
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        product_data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'image': request.FILES.get('image')
        }

        is_valid, error_messages = validate_product_upload(product_data)
        if not is_valid:
            return Response({"error": error_messages}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user

        serializer = ProductSerializer(data=product_data)
        if serializer.is_valid():
            # authenticate된 user를 author로 설정
            product = serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, productId):
        try:
            product = validate_product_update(request, productId)
        except PermissionDenied as e:
            return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)

        serializer = ProductDetailSerializer(
            product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, productId):
        try:
            product = validate_product_update(request, productId)
        except PermissionDenied as e:
            return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)

        product.delete()
        data = {"productId": f"상품 {productId}이 삭제되었습니다."}
        return Response(data, status=status.HTTP_200_OK)
