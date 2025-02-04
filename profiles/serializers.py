from rest_framework import serializers
from .models import Profile
from recipes.models import Recipe

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    # provides a count of recipes belonging to the profile
    recipes_count = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_recipes_count(self, obj):
        return Recipe.objects.filter(owner=obj.owner).count()

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'name', 'content', 'image', 'is_owner',
            'recipes_count'
        ]