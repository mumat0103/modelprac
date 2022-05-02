import imp
from statistics import mode
from django.db import models
from django.conf import settings
import os

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.CharField(max_length=4, default="***")
    author_email = models.CharField(max_length=50, default="wsx2138@naver.com")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = "blog/", blank="True", null="True")

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]
    
    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Blog, self).delete(*args, **kargs)