from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.CharField(max_length=4, default="***")
    author_email = models.CharField(max_length=50, default="wsx2138@naver.com")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]