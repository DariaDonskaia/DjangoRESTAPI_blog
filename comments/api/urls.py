from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from comments.api import view

urlpatterns = [
    path('api/comments/<int:pk>/', view.CommentDetail.as_view()),
    path('api/articles/<int:pk>/', view.ArticleDetailAPIView.as_view()),
    path('api/articles', view.add_article),
    path('api/comments/create', view.CommentCreateAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)