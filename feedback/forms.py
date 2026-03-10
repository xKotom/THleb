from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text', 'category']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Ваше сообщение...'}),
            'category': forms.TextInput(attrs={'placeholder': 'Категория (необязательно)'}),
        }
