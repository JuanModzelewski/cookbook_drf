from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class Review(models.Model):
    STAR_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=STAR_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Review by {self.user} on {self.recipe}'
