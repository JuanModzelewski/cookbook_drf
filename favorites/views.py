from rest_framework import generics, permissions
from cookbook_drf.permissions import IsOwnerOrReadOnly
from favorites.models import Favorite
from favorites.serializers import FavoriteSerializer


class FavoriteList(generics.ListCreateAPIView):
    """
    List all favorites or create a favorite if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FavoriteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a favorite, or delete it if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()