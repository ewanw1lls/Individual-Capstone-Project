from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django import forms

STATUS = ((0, "Draft"), (1, "Published"))


# Models here.


class Court(models.Model):
    INDOOR = 'Indoor'
    OUTDOOR = 'Outdoor'
    COURT_CHOICES = [
        (INDOOR, 'Indoor'),
        (OUTDOOR, 'Outdoor'),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="courts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    rating = models.DecimalField(
        max_digits=3, decimal_places=1,
        null=True, blank=True,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ]
    )  # Rating from 0.0 to 10.0
    profile_image = CloudinaryField(
        'image', default='placeholder'
    )  # Court image
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Indoor or Outdoor
    court_type = models.CharField(
        max_length=7,
        choices=COURT_CHOICES,
        default=OUTDOOR,
    )

    # going to need fields for location,
    # (longitude/latitude/address),

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Review(models.Model):
    Court = models.ForeignKey(
        Court, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.author}"


class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = [
            "title", "content", "profile_image",
            "rating", "excerpt", "court_type"
        ]
