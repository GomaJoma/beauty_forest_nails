from django.forms import Form, ModelForm
from .models import Review


class AddReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text']
