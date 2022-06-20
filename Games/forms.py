from django import forms
from .models import Game


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['title', 'description', 'type', 'fsk', 'creator', 'date_published']
        widgets = {
            'type': forms.Select(choices=Game.Genre),
            'fsk': forms.Select(choices=Game.Fsk),
            'user': forms.HiddenInput(),
        }
