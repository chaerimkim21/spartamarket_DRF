from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title', 
            'content', 
            'created_at', 
            'updated_at', 
            'image', 
            'view_count',
            'author',
        )
        read_only_fields = ('author',) # author field는 read_only로 설정해 로그인된 user가 author가 될 수 있도록 함

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'content', 'image']  # Include the fields you want to update

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.image = validated_data.get('image', instance.image)

        instance.save()
        return instance