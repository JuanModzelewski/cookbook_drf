from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import MediaCloudinaryStorage

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.JSONField()
    cooking_instructions = models.TextField()
    recipe_image = models.ImageField(
        upload_to='images/',
        storage=MediaCloudinaryStorage(),
        default='../default_post_i7i1x4',
        blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner}\'s recipe: {self.title}'
