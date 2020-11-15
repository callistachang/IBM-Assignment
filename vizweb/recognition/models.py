from django.db import models
from datetime import datetime
import os

# Create your models here.


def get_image_upload_path(instance, filename):
    now = datetime.now()
    return f"uploads/{now.strftime('%Y-%m-%d_%H-%M-%S')}_{instance.name}{instance.get_image_extension()}"


class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_image_extension(self):
        _, extension = os.path.splitext(self.image.name)
        return extension
