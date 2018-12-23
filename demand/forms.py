from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Comments, Demand, App


class CommentForm(forms.ModelForm):
    """Форма добавления комментария к требованию
    """
    class Meta:
        model = Comments
        fields = ('text', )
        widgets = {
            'text': SummernoteWidget(),
        }


class DemandForm(forms.ModelForm):
    """Форма добавления и редактирования требований
    """
    class Meta:
        model = Demand
        fields = ('title', 'for_apps', 'priority', 'description', 'status')
        widgets = {
            'title': forms.TextInput(),
            'for_apps': forms.SelectMultiple(),
            'priority': forms.Select(),
            'description': SummernoteWidget(),
            'status': forms.Select(),
        }


class AppForm(forms.ModelForm):
    """Форма добавления и редактирования приложений
    """
    class Meta:
        model = App
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(),
        }
