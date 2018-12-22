from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Comments, Demand


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
        fields = ('title', 'for_apps', 'description', 'status')
        widgets = {
            'title': forms.TextInput(),
            'for_apps': forms.SelectMultiple(),
            'description': SummernoteWidget(),
            'status': forms.Select(),
        }
