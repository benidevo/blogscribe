from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.articles.models import Article
from core_apps.common.models import TimeStampedModel

User = get_user_model()


class Rating(TimeStampedModel):
    RATING_CHOICES = [
        (1, "Poor"),
        (2, "Fail"),
        (3, "Good"),
        (4, "Very Good"),
        (5, "Excellent"),
    ]
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="ratings"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    review = models.TextField(blank=True)

    class Meta:
        unique_together = ("article", "user")
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")

    def __str__(self) -> str:
        return f"{self.user.first_name} rated {self.article.title} as {self.get_rating_display}"
