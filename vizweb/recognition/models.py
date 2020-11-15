from django.db import models
from datetime import datetime


class Image(models.Model):
    image = models.ImageField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ImageLabel(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="labels")
    label = models.CharField(max_length=50)
    score = models.FloatField()

    class Meta:
        ordering = ["-score"]
