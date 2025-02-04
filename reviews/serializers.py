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
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    recipe_title = serializers.ReadOnlyField(source='recipe.title')

    def get_created_at(self, obj):
        """
        Returns the time the review was created in a human-readable format
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Returns the time the review was last updated in a human-readable format
        """
        return naturaltime(obj.updated_at)

    def get_is_owner(self, obj):
        """
        Returns True if the user is the owner of the review
        """
        request = self.context['request']
        return request.user == obj.owner

    def create(self, validated_data):
        """
        Creates a new review and saves it to the database.
        If the user has already reviewed the recipe, raises a validation error.
        """
        request = self.context['request']
        user = request.user
        recipe = validated_data['recipe']

        # Check if the user has already reviewed this recipe
        if Review.objects.filter(owner=user, recipe=recipe).exists():
            raise serializers.ValidationError(
                "You have already reviewed this recipe.")

        review = Review(
            owner=user,
            recipe=recipe,
            rating=validated_data['rating'],
            comment=validated_data['comment']
        )
        review.save()
        return review

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'recipe', 'recipe_title',
            'rating', 'comment', 'created_at', 'updated_at',
            ]


class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for a detailed view of a review.
    This serializer includes the id of the recipe which the review is for.
    """
    recipe = serializers.ReadOnlyField(source='recipe.id')
