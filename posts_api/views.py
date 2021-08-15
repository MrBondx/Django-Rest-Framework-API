from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from . models import Post
from .serializers import PostSerializer
'''
@api_view(['GET'])
def routes(request):
    routes = [
    {
        'Endpoint': 'posts',
        'method': 'GET',
        'body': None,        
        'Description': 'Returns all posts objects in an array'
    },
    {
        'Endpoint': 'posts/<id>',
        'method': 'GET',
        'body': None,        
        'Description': 'Returns a single post object by its id'
    },
    {
        'Endpoint': 'create',
        'method': 'POST',
        'body': {'body' : ''},        
        'Description': 'Creates a post new post object'
    },
    {
        'Endpoint': 'posts/<id>/edit',
        'method': 'POST',
        'body': {'body' : ''},        
        'Description': 'Creates a post new post object'
    },
    {
        'Endpoint': 'posts/<id>/delete',
        'method': 'DELETE',
        'body': None,        
        'Description': 'Deletes a post object'
    }
    ]
    return Response(routes)
'''
@api_view(['GET'])
def posts_api(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_api(request, post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):    
    post = Post.objects.create(
        title = request.data.get('title'),
        body = request.data.get('body')
        )
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return Response('Post deleted')





