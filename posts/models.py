from django.db import models
from users.models import UserModel


class PostModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"Post {self.id} by {self.user.username}"
