from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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
        # filter out recipes with no initial
        # comments using Q (query object)
        # filter out empty comments using ~ (negation)
        # filter out parent comments
        # separates review comments from star rating
        comment_count=Count(
                'reviews__comments',
                filter=Q(reviews__comments__comment__isnull=False)
                & ~Q(reviews__comments__comment='')
                & Q(reviews__comments__parent__isnull=True)
            )
        ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
        ]
    filterset_fields = [
        'favorites__owner__profile',
        'reviews__owner__profile',
        'owner__profile',
        ]
    search_fields = ['title', 'description']
    ordering_fields = ['favorite_count', 'review_count', 'comment_count']

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except Exception as e:
            print(f"Error creating recipe: {e}")
            raise


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
