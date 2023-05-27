from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.articles.models import Article
from core_apps.common.models import TimeStampedModel

User = get_user_model()


class ResponseModel(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responses")
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="responses"
    )
    parent_response = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )
    content = models.TextField(verbose_name=_("Response content"))

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")

    def __str__(self) -> str:
        return f"{self.user.first_name} commented on {self.article.title}"
