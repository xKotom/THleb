from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ProfileTag


class RegisterForm(UserCreationForm):
    card_number = forms.CharField(
        label='Номер клубной карты',
        max_length=50,
        required=False,
        help_text='Выдаётся после трёх покупок в пекарне. Можно добавить позже в личном кабинете.',
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


class CardForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['card_number']
        labels = {
            'card_number': 'Номер клубной карты',
        }
        help_texts = {
            'card_number': 'Выдаётся после трёх покупок в пекарне.',
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
