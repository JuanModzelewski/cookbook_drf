from django.db.models import Count
from rest_framework import generics, permissions, filters
from cookbook_drf.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.annotate(
        recipes_count=Count('owner__recipe', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['recipes_count']


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        recipes_count=Count('owner__recipe', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    