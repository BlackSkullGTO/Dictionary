from django.forms import ModelForm

from .models import Word

class WordCreateForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Word
        fields = [
            'word', 'translate'
        ]
        labels = {
            "word": "Слово на английском",
            "translate": "Перевод на русский",
        }

class WordUpdateForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Word
        fields = [
            'word', 'translate', 'active'
        ]
        labels = {
            "word": "Слово на английском",
            "translate": "Перевод на русский",
            "active": "Активно",
        }