from django import forms

from .models import Comments


class CommentForm(forms.ModelForm):
    """Форма добавления комментария к требованию
    """
    class Meta:
        model = Comments
        fields = ('text', )
        labels = ('Добавить комментарий', )
        widgets = {
            'text': forms.Textarea(attrs={'cols': '40',
                                          'rows': '3'}),
        }
