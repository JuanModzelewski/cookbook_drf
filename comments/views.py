from rest_framework import generics, permissions
from cookbook_drf.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all().filter(parent=None)

    def get_serializer_context(self):
        """
        Adds the request to the serializer context for use in validation.
        """
        return {'request': self.request}
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_serializer_context(self):
        """
        Adds the request to the serializer context for use in validation.
        """
        return {'request': self.request}