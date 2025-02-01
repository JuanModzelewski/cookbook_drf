from rest_framework import serializers
from .models import Comment
from reviews.models import Review
from django.contrib.humanize.templatetags.humanize import naturaltime

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    recipe_title = serializers.ReadOnlyField(source='review.recipe.title')
    review = serializers.PrimaryKeyRelatedField(queryset=Review.objects.all())
    review_comment = serializers.SerializerMethodField()
    parent = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False, allow_null=True)
    replies = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        """
        Returns the time the comment was created
        """
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        """
        Returns the time the comment was last updated
        """
        return naturaltime(obj.updated_at)
    
    def get_review_comment(self, obj):
        """
        Returns the comment associated with the review
        Only displayed in the parent comment
        """
        if obj.parent is None:
            return obj.review.comment
        return None
    
    def get_replies(self, obj):
        """
        Returns a list of replies to the comment
        """
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return None
    
    def get_is_owner(self, obj):
        """
        Returns True if the user is the owner of the comment
        """
        request = self.context.get('request', None)
        if request:
            return obj.owner == request.user
        return None

    def validate(self, data):
        """
        Checks if the parent comment belongs to the same review as the review
        being commented on.
        """
        parent = data.get('parent')
        review = data.get('review')
        if parent and parent.review != review:
            raise serializers.ValidationError("Reply's parent comment must belong to the same review.")
        elif not parent and not review.comment:
            raise serializers.ValidationError("Comments can only be added if the review has an initial comment.")
        return data
    
    def create(self, validated_data):
        user = self.context['request'].user
        comment = Comment(
            owner=user,
            review=validated_data.get('review'),
            parent=validated_data.get('parent'),
            comment=validated_data.get('comment')
        )
        comment.save()
        return comment
    
    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'review', 'recipe_title', 'review_comment', 'comment', 'created_at',
            'updated_at', 'replies', 'parent',
        ]