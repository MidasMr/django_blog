from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from posts.models import Post
from .pagination import PageNumberLimitPagination
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = PageNumberLimitPagination

    def perform_create(self, serializer):
        print(self.request.data)
        author = self.request.user
        if 'file' in self.request.data:
            print(self.request.data['file'])
            serializer.save(
                author=author, image=self.request.data['file']
            )
        serializer.save(author=author)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = PageNumberLimitPagination
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(
            Post, id=self.kwargs.get('post_id')
        )
        serializer.save(
            author=self.request.user, post=post
        )
