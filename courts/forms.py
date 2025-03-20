from .models import Review, Court
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = ["title", "content", "profile_image", "rating", "excerpt", "field_type"]
