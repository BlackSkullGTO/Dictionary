from django import forms

class CreateTestForm(forms.Form):
    word_count = forms.IntegerField(label='Количество слов')
