from rest_framework import serializers
from .models import Review
from django.contrib.humanize.templatetags.humanize import naturaltime

class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for Review model.
    This serializer is used to display review information to users.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'recipe', 'rating',
            'comment', 'created_at', 'updated_at',
            'is_owner', 'profile_id', 'profile_image',
            'recipe',
            ]
        
class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for a detailed view of a review.
    This serializer includes the id of the recipe which the review is for.
    """
    recipe = serializers.ReadOnlyField(source='recipe.id')
