from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name="poster")
    date_published = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    text = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comenter")
    date_published = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text[:50]+"..."

#username: mehtab, password:Passprofile@1, email:ahmadmehtab064@gmail.com

    



