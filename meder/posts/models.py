from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db import models
# from django.contrib.auth.models import User
# from django.db.models  import Model

class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='post.jpg', upload_to='profile_image')

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("posts-detail", kwargs={"pk": self.pk})


