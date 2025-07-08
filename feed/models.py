from django.db import models
from users.models import UserModel
from posts.models import PostModel


class FeedModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="feeds")
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     verbose_name = "Feed"
    #     verbose_name_plural = "Feeds"

    # def __str__(self):
    #     return f"Feed of {self.user.username} with post {self.post.id}"
