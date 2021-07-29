from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from rest_framework import response
from rest_framework.views import APIView
from comments.api import serializers
from comments.models import Comment, Article
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST', 'GET'])
def add_article(request):
    if request.method == 'GET':
        try:
            queryList = Article.objects.all()
        except Article.DoesNotExist: 
            return response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.ArticleSerializer(queryList, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(RetrieveAPIView):
    
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleDetailSerializer


class CommentCreateAPIView(CreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CommentDetail(RetrieveAPIView):

    queryset = Comment.objects.all()
    serializer_class = serializers.CommentDetailSerializer
    lookup_field = 'pk'
