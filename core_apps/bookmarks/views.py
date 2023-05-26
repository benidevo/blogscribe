from uuid import UUID

from django.db import IntegrityError
from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound, ValidationError

from core_apps.articles.models import Article

from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkCreateView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        article_id = self.kwargs.get("article_id")
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
            except Article.DoesNotExist:
                raise ValidationError("Invalid article_is provided")
        else:
            raise ValidationError("article_id is required")

        try:
            serializer.save(article=article, user=self.request.user)
        except IntegrityError:
            raise ValidationError("You have already bookmarked this article")


class BookmarkDestroyView(generics.DestroyAPIView):
    queryset = Bookmark.objects.all()
    lookup_field = "id"
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        article_id = self.kwargs.get("article_id")

        try:
            UUID(str(article_id), version=4)
        except ValueError:
            raise ValidationError("Invalid article_id provided")

        try:
            bookmark = Bookmark.objects.get(user=user, article__id=article_id)
        except Bookmark.DoesNotExist():
            raise NotFound("Bookmark not found or does not belong to you")

        return bookmark

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.user != user:
            raise ValidationError(
                "You can not delete a bookmark that does not belong to you"
            )

        instance.delete()
