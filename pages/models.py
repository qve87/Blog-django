from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=155)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField("auth.User", related_name="blog_posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pages_detail", kwargs={"pk": self.pk})

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ["-created"]
