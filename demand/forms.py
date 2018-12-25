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
        fields = ('title', 'for_apps', 'status', 'priority', 'description')
        widgets = {
            'title': forms.TextInput(),
            'for_apps': forms.SelectMultiple(),
            'status': forms.Select(),
            'priority': forms.Select(),
            'description': SummernoteWidget(),
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
