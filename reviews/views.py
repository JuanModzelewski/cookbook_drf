from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from cookbook_drf.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['recipe']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
