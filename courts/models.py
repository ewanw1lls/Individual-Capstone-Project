from django.db import models
# from blog walkthrough v
from django.contrib.auth.models import User   

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)  # Rating from 0.0 to 10.0
    image = models.ImageField(upload_to='court_images/', null=True, blank=True)  # Court image

    def __str__(self):
        return self.title