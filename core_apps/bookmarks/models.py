from django.contrib.auth import get_user_model
from django.db import models

from core_apps.articles.models import Article
from core_apps.common.models import TimeStampedModel

User = get_user_model()


class Bookmark(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="bookmarks"
    )

    class Meta:
        unique_together = ["user", "article"]

    def __str__(self) -> str:
        return f"{self.user.first_name} bookmarked {self.article.title}"
