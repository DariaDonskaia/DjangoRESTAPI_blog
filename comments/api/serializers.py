from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from comments.models import Comment, Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'articleId', 'parent']


class CommentDetailSerializer(serializers.ModelSerializer):
        replies = SerializerMethodField()
        class Meta:
            model = Comment
            fields = ['id', 'content','articleId',  'parent', 'replies']
           
        def get_replies(self, obj):
            return CommentDetailSerializer(obj.children(), many=True).data


class ArticleDetailSerializer(serializers.ModelSerializer):
    comments = SerializerMethodField()
    class Meta:
        model = Article
        fields = ['id', 'comments' ]

    def get_comments(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentDetailSerializer(c_qs, many=True).data
        return comments
