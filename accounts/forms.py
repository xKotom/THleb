from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ProfileTag


class RegisterForm(UserCreationForm):
    card_number = forms.CharField(
        label='Номер клубной карты',
        max_length=50,
        help_text='Выдаётся после трёх покупок в пекарне.',
    )
    nickname = forms.CharField(label='Имя или псевдоним', max_length=100)

    class Meta:
        model = User
        fields = ['username', 'nickname', 'card_number', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'date_of_birth', 'photo', 'bio']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class TagForm(forms.Form):
    tags = forms.CharField(
        label='Интересы',
        widget=forms.Textarea(attrs={
            'placeholder': 'кофе, настольные игры, чтение, утренние прогулки',
            'rows': 3,
        }),
        help_text='Введите теги через запятую.',
    )
