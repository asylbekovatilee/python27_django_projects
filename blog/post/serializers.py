from rest_framework.serializers import ModelSerializer
from .models import Post
from review.serializers import CommentSerializer

# вид отображение

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes.all().count()
        comments = instance.comments.all() # все комменты данные
        rep['comments'] = CommentSerializer(comments, many=True).data
        return rep 
    
        