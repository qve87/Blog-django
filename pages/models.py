from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=155)
    body = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pages_detail", kwargs={"pk": self.pk})
