from rest_framework import generics, permissions, filters
from .models import Recipe
from .serializers import RecipeSerializer
from cookbook_drf.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class RecipeList(generics.ListCreateAPIView):
    """
    List recipes or create a recipe if logged in
    The perform_create method associates the recipe with the logged in user.
    """
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.annotate(
        favorite_count=Count('favorites', distinct=True)
        ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a recipe and edit or delete it if you own it.
    """
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recipe.objects.annotate(
        favorite_count=Count('favorites', distinct=True)
        ).order_by('-created_at')