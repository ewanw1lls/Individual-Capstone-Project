from .models import Review, Court
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = [
            'title', 'content', 'rating',
            'profile_image', 'excerpt', 'court_type'
        ]

    court_type = forms.ChoiceField(
        choices=Court.COURT_CHOICES,
        widget=forms.RadioSelect,
        label="Court Type",
    )
