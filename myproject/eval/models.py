from django.db import models

# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=50)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.caption}"