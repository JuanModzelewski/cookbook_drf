from rest_framework import generics, permissions, filters
from .models import Recipe
from .serializers import RecipeSerializer
from cookbook_drf.permissions import IsOwnerOrReadOnly
from django.db.models import Count, Q


class RecipeList(generics.ListCreateAPIView):
    """
    List recipes or create a recipe if logged in
    The perform_create method associates the recipe with the logged in user.
    """
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.annotate(
        favorite_count=Count('favorites', distinct=True),
        review_count=Count('reviews', distinct=True),
        comment_count=Count(
            
            # filter out recipes with no initial comments using Q (query object)
            # filter out empty comments using ~ (negation)
            # filter out parent comments
            # separates review comments from star rating
            
                'reviews__comments',
                filter=Q(reviews__comments__comment__isnull=False)
                & ~Q(reviews__comments__comment='')
                & Q(reviews__comments__parent__isnull=True)
            )
        ).order_by('-created_at')
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a recipe and edit or delete it if you own it.
    """
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recipe.objects.annotate(
        favorite_count=Count('favorites', distinct=True),
        review_count=Count('reviews', distinct=True),
        comment_count=Count(
                'reviews__comments',
                filter=Q(reviews__comments__comment__isnull=False)
                & ~Q(reviews__comments__comment='')
                & Q(reviews__comments__parent__isnull=True)
            )
        ).order_by('-created_at')