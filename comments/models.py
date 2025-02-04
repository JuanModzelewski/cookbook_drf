from django.db import models
from django.contrib.auth.models import User
from reviews.models import Review


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(
        Review, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='replies',
        on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.parent:
            return f'Reply by {self.owner} on {self.review}'
        return f'Comment by {self.owner} on {self.review}'
