from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'content',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(),
        }


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('content',)

        widgets = {
            'user': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(),
        }