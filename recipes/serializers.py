from rest_framework import serializers
from recipes.models import Recipe
from favorites.models import Favorite

def validate_image(image):
    # Check image size (limit to 2MB)
    if image.size > 2 * 1024 * 1024:
        raise serializers.ValidationError("Image file size may not exceed 2MB.")
    # Check image dimensions (limit to max width and height of 4096px)
    if hasattr(image, 'image'):
        width, height = image.image.size
        if width > 4096 or height > 4096:
            raise serializers.ValidationError("Image dimensions may not exceed 4096x4096 pixels.")
    return image

class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image.url')
    recipe_image = serializers.ImageField(validators=[validate_image], required=False)
    favorite_id = serializers.SerializerMethodField()
    favorite_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_favorite_id(self, obj):
        """
        Returns the id of the favorite associated with the recipe
        If the user is not authenticated, returns None
        Will allow all favorite recipes to be identified and displayed
        """
        user = self.context['request'].user
        if user.is_authenticated:
            favorites = Favorite.objects.filter(owner=user, recipe=obj).first()
            return favorites.id if favorites else None
        return None
    

    class Meta:
        model = Recipe
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'title', 'description',
            'ingredients', 'cooking_instructions',
            'recipe_image', 'created_at', 'updated_at', 
            'favorite_id', 'favorite_count',
        ]