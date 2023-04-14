from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Like
from post.models import Post, User

@api_view(['POST'])
def toggle_like(request, id):
    user_id = request.data.get('user')
    if not user_id:# user_id = None
        return Response({"user":["this is field is required"]}, status=404)
    user = get_object_or_404(User, id=user_id)
    post = get_object_or_404(Post, id=id)
    if Like.objects.filter(user=user, post=post).exists():
        # усли лайк есть то удаляем его
        Like.objects.filter(user=user, post=post).delete()
    else:
        Like.objects.create(user=user, post=post)
    return Response(status=201)