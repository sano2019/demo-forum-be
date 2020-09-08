from rest_framework.serializers import ModelSerializer
from .models import Post, Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title',
            'country',
        )


class PostSerializer(ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Post
        fields = (
            'view_count',
            'category'
        )