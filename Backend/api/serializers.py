from rest_framework import  serializers
from .models import Post , Category , Comment

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Post
        fields ='__all__'
        category_name = serializers.CharField(source='category.name', read_only=True)
        
# For creating a new post with
class CommentSerializer(serializers.ModelSerializer):
    
    class  Meta:
        
        model=Comment
        fields='__all__'
